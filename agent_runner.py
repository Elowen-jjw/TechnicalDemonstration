# agent_runner.py
from pathlib import Path
import time
import argparse
from openai import OpenAI

# ========================== UTIL FUNCTIONS ==========================
def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def write_file(path: Path, content: str):
    path.write_text(content, encoding="utf-8")

def extract_imports(code: str) -> str:
    lines = code.splitlines()
    import_lines = []
    for line in lines:
        if line.strip().startswith("#"): continue
        if line.strip().startswith("def "):
            break
        import_lines.append(line)
    return "\n".join(import_lines).strip()

def extract_test_cases(code: str) -> list[str]:
    lines = code.splitlines()
    test_cases = []
    i = 0
    n = len(lines)

    while i < n:
        if lines[i].lstrip().startswith("@pytest"):
            start = i
            i += 1

            while i < n and not lines[i].lstrip().startswith("def "):
                i += 1

            if i < n and lines[i].lstrip().startswith("def "):
                i += 1
                while i < n:
                    current_line = lines[i]
                    if current_line.strip() == "":
                        i += 1
                        continue
                    if current_line.startswith(" ") or current_line.startswith("\t"):
                        i += 1
                    else:
                        break
                test_cases.append("\n".join(lines[start:i]))

        elif lines[i].lstrip().startswith("def "):
            start = i
            i += 1
            while i < n:
                current_line = lines[i]
                if current_line.strip() == "":
                    i += 1
                    continue
                if current_line.startswith(" ") or current_line.startswith("\t"):
                    i += 1
                else:
                    break
            test_cases.append("\n".join(lines[start:i]))
        else:
            i += 1

    return test_cases

def add_imports_to_tests(imports: str, test_bodies: str) -> str:
    return f"{imports}\n\n{test_bodies}"

def build_module_prompt(modules: list[str], names: list[str], semantics: str) -> str:
    prompt_parts = []
    if modules:
        prompt_parts.append(f"I will provide {len(modules)} Python modules, then a series of unit tests targeting those modules.")
        prompt_parts.append(f"Here is the first Python module_0 {names[0]}:\n{modules[0]}\n\n")
        for idx, (mod, name) in enumerate(zip(modules[1:], names[1:]), start=1):
            prompt_parts.append(f"Here is the next Python module_{idx} {name}:\n{mod}\n\n")
        prompt_parts.append(f"{semantics}\n\n")
    return "\n\n".join(prompt_parts)

def load_prompt_lines(prompt_file: Path) -> list[str]:
    paragraphs = []
    current_paragraph = []

    for line in prompt_file.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped:
            current_paragraph.append(stripped)
        elif current_paragraph:
            paragraphs.append(" ".join(current_paragraph))
            current_paragraph = []

    if current_paragraph:
        paragraphs.append(" ".join(current_paragraph))

    return paragraphs

# ========================== LLM AGENT CLASS ==========================
class TestImprovementAgent:
    #LLM agent that keeps a static system prompt (with module context) and
        # sends a fresh user message each call. No conversation history is
        # accumulated, which avoids token bloat while still giving the model the

    def __init__(self, api_key: str, module_prompt: str, model: str = "gpt-4o"):
        self.client = OpenAI(api_key=api_key)
        self.base_messages = [
            {
                "role": "system",
                "content": (
                    f"You are an expert software engineer improving test code readability."
                    f"{module_prompt}"
                ),
            }
        ]
        self.model = model

    def improve_test(self, test_case: str, change_prompt: str, is_step: bool) -> str:
        # Send ONE user message with the test + change instruction.
        # No previous user/assistant messages are persisted.
        if is_step:
            user_msg = (
                f"Here is a pytest test case:\n{test_case}\n"
                f"Please understand the logic and semantic. Then, improve the readability of the function while strictly preserving semantics and grammar correctness by the following changes : {change_prompt}. \n"
                f"Output only the modified function. Return modified python code only without markdown formatting (no ```python ... ```), and Do not add any import statements. "
                # f"we sequentially apply the enhancement rules. Each rule is checked for applicability—if a match is found, the corresponding transformation is applied; otherwise, the rule is skipped without modification.:\n{change_prompt}\n"
            )
        else:
            user_msg = (
                f"Please check and correct only grammatical or syntax errors in the following Python module. "
                f"Do not change code structure or logic. Only add necessary missing import statements. "
                f"Output the corrected code only, without explanations or markdown formatting (no ```python ... ```).\n{test_case}\n"
            )

        messages = self.base_messages + [{"role": "user", "content": user_msg}]

        # print("OpenAI message: \n", messages[:500], "...\n")

        try:
            resp = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.2,
                n=1,
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            print(f"OpenAI call failed: {e}")
            return ""

# ========================== MAIN PIPELINE ==========================
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--modules', nargs='+', required=True, help='List of module file paths')
    parser.add_argument('--test', required=True, help='Path to the test file')
    parser.add_argument('--changes_file', required=True, help='File where each line is a prompt change')
    parser.add_argument('--semantics', required=True, help='Path to semantic prompt file')
    parser.add_argument('--output_dir', default='improved_tests', help='Directory to save output')
    args = parser.parse_args()

    module_paths = [Path(p) for p in args.modules]
    test_path = Path(args.test)
    semantic_path = Path(args.semantics)
    changes_file = Path(args.changes_file)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    module_codes = [read_file(f) for f in module_paths]
    module_names = [f.name for f in module_paths]
    semantic_prompt = read_file(semantic_path)
    module_prompt = build_module_prompt(module_codes, module_names, semantic_prompt)
    changes_lines = load_prompt_lines(changes_file)

    import_block = extract_imports(read_file(test_path))
    test_cases = extract_test_cases(read_file(test_path))

    # Before execution, must complete api-key value.
    agent = TestImprovementAgent(api_key="",
                                 module_prompt=module_prompt,
                                 model="gpt-4o")

    for step_idx, change_prompt in enumerate(changes_lines, start=1):
        improved_tests = []

        for i, test_case in enumerate(test_cases, start=1):
            print(f"[Step {step_idx}] Processing test {i}/{len(test_cases)}...")
            improved = agent.improve_test(test_case, change_prompt, True)
            improved_tests.append(improved)
            time.sleep(1.5)

        merged = "\n\n".join(improved_tests)
        full_test_file = add_imports_to_tests(import_block, merged)
        full_test_file = agent.improve_test(full_test_file, "", False)

        output_path = output_dir / f"{test_path.stem}_improved{step_idx}.py"
        write_file(output_path, full_test_file)
        print(f"✓ Output file: {output_path.name}")

        test_cases = extract_test_cases(full_test_file)

    print("✅ Finished!")


if __name__ == "__main__":
    main()
