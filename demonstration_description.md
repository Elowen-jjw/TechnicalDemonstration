# Technical Demonstration: Automated Test Readability Enhancement

We present an **automated agent** that replicates and extends the method from Improving Test Code Readability with LLMs. While the original approach relies on manual prompting in ChatGPT, our system automates the entire process using the OpenAI API (GPT-4o), enabling fully hands-free test enhancement.

Due to the OpenAI API’s limitation on file uploads, we convert code files to string format. Surprisingly, converting the code to strings and sending it via API can be more precise than using ChatGPT’s interface directly.

## Semantic Extension
A key contribution of our implementation is the incorporation of semantic information about the module under test—such as control flow, data flow, statement purposes, and variable types and roles—via an additional prompt file `semantic_analysis_mut.txt`. With this guidance, the model tends to generate clearer function and variable names, stick to a consistent style, and avoid vague or inappropriate labels. For now, this semantic information is passed in plain text—but it could later be replaced with structured data from static analysis tools.

## Transformation Procedure
Our prompting strategy follows the same iterative design as the original work. We apply a sequence of prompt-based transformations to unit tests, one step at a time. The output from each transformation serves as the input for the next:
> 🔁 Apply prompts → Regenerate test file → Extract new test cases → Apply next prompt
All transformations are defined in all_changes.txt, where each block (separated by blank lines) corresponds to a specific transformation.
The following transformations are applied in order:
- Literal Extraction: Extracting repeated literals or magic values into named constants.
- Structure Segmentation: Separating test logic into # Arrange, # Act, and # Assert sections.
- Assertion Merging: Merging redundant field-by-field assertions into deep equality checks.
- Function Renaming: Renaming test function to be concise and self-descriptive.
- Variable Renaming: Renaming local variables to reflect semantic roles.
- Dead Code Removal: Removing unused assignments.
- Comment Enhancement: Add an intent comment at the top and concise inline comments to clarify logic.

After each tranformation, the output is saved to `improved_test_suites/`, making it easy to inspect the effect of individual transformations.

## Usage

| Argument         | Description                                                  |
|------------------|--------------------------------------------------------------|
| `--modules`      | Python files of the modules under test (supports multiple)   |
| `--test`         | The initial test suites                                      |
| `--changes_file` | A text file where each paragraph is a transformation prompt  |
| `--semantics`    | A prompt file describing semantic information of the modules |
| `--output_dir`   | Directory for saving outputs after each transformation step  |

Run `agent_runner.py` with the parameters below, or directly use `overall.py` to execute a preconfigured demonstration. The script will automatically apply each transformation step-by-step and generate refined test suites.

## Example Results:

For `test_string_utils_validation.py`, we compare results from the original method and our extended agent-based version. Codes below show the same test case (`Version 1` = enhanced, `Version 2` = original):
<img width="1173" alt="image" src="https://github.com/user-attachments/assets/ca4f86d0-c3d0-4d8b-9866-bc2f57f42aef" />

<img width="1217" alt="image" src="https://github.com/user-attachments/assets/c38e7ec0-df31-4e3c-91d5-1f23af960f4c" />

For `test_httpie_sessions.py`, the contrast is similarly shown:
<img width="1151" alt="image" src="https://github.com/user-attachments/assets/64788450-0d47-4594-9b77-18491a5f4589" />

<img width="978" alt="image" src="https://github.com/user-attachments/assets/abede99d-e7c1-4333-8766-59b7f64576b6" />

The summary comparison is as follows:
| Aspect         | Version 1                            | Version 2                        | Comparison Result     |
|----------------|--------------------------------------|----------------------------------|------------------------|
| Readability    | ✅ Clearly segmented, intent stated   | ❌ Mixed structure, no intent    | Significant improvement |
| Naming Clarity | ✅ Descriptive and easy to follow     | ❌ Vague or templated            | Noticeable enhancement |
| Comment Quality| ✅ Clear intent and organized notes   | ❌ Sparse or code-repeating comments | Better structure     |

However, for `test_queue_example.py`, the agent did not yield significant improvements in readability, likely due to the test’s simple structure or limited room for enhancement.


