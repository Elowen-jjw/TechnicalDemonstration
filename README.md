### Technical Demonstration: Automated Test Readability Enhancement

We **implement an automated agent** that replicates and extends the approach from Improving Test Code Readability with LLMs. The original work uses manual prompts through ChatGPT to rewrite test code for better readability. In contrast, our implementation automates this process end-to-end using the OpenAI API (GPT-4o), without requiring user interaction. Because the openai api can not support file upload, in this automation work, we parse it transferred to the str code, in some extent, this method is more accurate than through
the ChatGPT interface with the Code Interpreter plug-in. 

**As an extension to the original work, we provide the LLM with semantic information (i.e. control flow, data flow, statement purposes and variable types and roles) about the module-under-test, detailed in an additional prompt `semantic_analysis_mut.txt`. This helps the model avoid misleading or overly generic names during renaming and improves consistency across transformations. While this semantic guidance is currently represented textually, future work could integrate structured representations extracted via static analysis.** 

The prompting structures is mostly identical to the original work. We iteratively applies a sequence of readability transformations to unit tests, guided by prompt instructions. This means:
> 🔁 Sequentially apply prompts → regenerate test file → extract new test cases → apply next prompt
Each transformation is defined in a text file `all_changes.txt`, where blocks are separated by blank lines and executed in order. These transformations include:
- Extracting repeated literals or magic values into named constants.
- Separating test logic into # Arrange, # Act, and # Assert sections.
- Merging redundant field-by-field assertions into deep equality checks.
- Renaming tests to be concise and self-descriptive.
- Renaming local variables to reflect semantic roles.
- Removing unused assignments.
- Adding clear inline comments and an intent header at the top of each test.

After one tranformation, one output file will be saved in `improved_test_suites/`, making it easy to inspect the effect of each transformation in isolation.

## Usage

| Argument         | Description                                                  |
|------------------|--------------------------------------------------------------|
| `--modules`      | Python files of the modules under test (supports multiple)   |
| `--test`         | The initial test file                                        |
| `--changes_file` | A text file where each paragraph is a transformation prompt  |
| `--semantics`    | A prompt file describing semantic information of the modules |
| `--output_dir`   | Directory for saving outputs after each transformation step  |

Run `agent_runner.py` with the parameters below, or directly use `overall.py` to execute a preconfigured demonstration. The script will automatically apply each transformation step-by-step and generate refined test suites.
