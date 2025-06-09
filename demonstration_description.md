# Technical Demonstration: Automated Test Readability Enhancement

The full source code and documentation are available at: [https://github.com/Elowen-jjw/TechnicalDemonstration](https://github.com/Elowen-jjw/TechnicalDemonstration) 

This repository includes:
- my full implementation of an automated pipeline for improving test readability using ChatGPT
- the improved test suites
- some notes of transformations that didn’t work as expected
- a new idea inspired by the professor’s original approach

In this work, I built an **automated agent** that replicates and extends the method from Improving Test Code Readability with LLMs. Unlike the original approach that required manual prompting in ChatGPT, my version uses the OpenAI API (GPT-4o) to run the entire process automatically.

Since the OpenAI API does not support file uploads, I convert code into strings before sending it. Surprisingly, this approach turned out to be more reliable than using the ChatGPT interface directly.

## Semantic Extension
A key contribution of my implementation is the incorporation of semantic information about the module under test—such as control flow, data flow, statement purposes, and variable types and roles—via an additional prompt file `prompts/semantic_analysis_mut.txt`. This additional input helps the model produce cleaner names, follow consistent conventions, and avoid unclear labels. At this stage, the semantic information is written manually in plain text to reflect the kinds of details that should be considered. In the future, this part can be replaced with output automatically extracted using static analysis tools.

## Transformation Procedure
I adopt a similar iterative strategy: each transformation step rewrites the test, and its result feeds into the next stage in the sequence.
> 🔁 Apply prompts → Regenerate test file → Extract new test cases → Apply next prompt
All transformations are defined in `prompts/all_changes.txt`, where each block (separated by blank lines) corresponds to a specific transformation.
The following transformations are applied in order:
- Literal Extraction: Extracting repeated literals or magic values into named constants.
- Structure Segmentation: Separating test logic into # Arrange, # Act, and # Assert sections.
- Assertion Merging: Merging redundant field-by-field assertions into deep equality checks.
- Function Renaming: Renaming test function to be concise and self-descriptive.
- Variable Renaming: Renaming local variables to reflect semantic roles.
- Dead Code Removal: Removing unused assignments.
- Comment Enhancement: Add an intent comment at the top and concise inline comments to clarify logic.

After each transformation, the output is saved to `improved_test_suites/`, making it easy to inspect the effect of individual transformations.

## Usage

| Argument         | Description                                                  |
|------------------|--------------------------------------------------------------|
| `--modules`      | Python files of the modules under test (supports multiple)   |
| `--test`         | The initial test suites                                      |
| `--changes_file` | A text file where each paragraph is a transformation prompt  |
| `--semantics`    | A prompt file describing semantic information of the modules |
| `--output_dir`   | Directory for saving outputs after each transformation step  |

Run `agent_runner.py` with the parameters below, or directly use `overall.py` to execute a preconfigured demonstration. The script will automatically apply each transformation step-by-step and generate refined test suites.

⚠️ **Note:** Before running the script, you need to set your OpenAI API key by editing the `agent_runner.py` file or by setting the `OPENAI_API_KEY` environment variable.

## Example Results:

### test_string_utils_validation.py
For `test_string_utils_validation.py`, I compare results from the original method and my extended agent-based version. The codes below show the same test case (`Version 1` = improved, `Version 2` = original):

Version 1:
<img width="1173" alt="image" src="https://github.com/user-attachments/assets/ca4f86d0-c3d0-4d8b-9866-bc2f57f42aef" />

Version 2:
<img width="1217" alt="image" src="https://github.com/user-attachments/assets/c38e7ec0-df31-4e3c-91d5-1f23af960f4c" />

### test_httpie_sessions.py
For `test_httpie_sessions.py`, the contrast is similarly shown:

Version 1:
<img width="1151" alt="image" src="https://github.com/user-attachments/assets/64788450-0d47-4594-9b77-18491a5f4589" />

Version 2:
<img width="978" alt="image" src="https://github.com/user-attachments/assets/abede99d-e7c1-4333-8766-59b7f64576b6" />

### test_queue_example.py
However, for `test_queue_example.py`, the agent did not yield significant improvements in readability, likely due to the simple structure of the test or limited room for enhancement.

### The summary comparison is as follows:
| Aspect                  | Version 1 (Enhanced)                                    | Version 2 (Original)                           |
| ----------------------- | ------------------------------------------------------- | ---------------------------------------------- |
| Structural Segmentation | Clearly segmented with `# Arrange`, `# Act`, `# Assert` | Structure present but not explicitly segmented |
| Intent Clarification    | Intent is explicitly described at the top               | Intent included but in docstring, less visible |
| Function Naming         | Function names are self-explanatory                     | Function names are generic or templated        |
| Comment Quality         | Short, clear, and targeted comments                     | Comments repeat code or are sparse             |
| Assertion Grouping      | Assertions grouped logically under labels               | Assertions are loosely placed                  |
