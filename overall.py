import subprocess

# Run this file to get the improved test suites saved in the directory 'improved_test_suites'.
# Run 'python agent_runner.py --help' to get the instructions for every parameter

commands = [
    [
        "python", "agent_runner.py",
        "--modules", "initial_test_suites/httpie_sessions/sessions.py", "initial_test_suites/httpie_sessions/dicts.py",
        "--test", "initial_test_suites/httpie_sessions/test_httpie_sessions.py",
        "--semantics", "prompts/prompt_semantic_analysis.txt",
        "--changes_file", "prompts/all_changes.txt",
        "--output_dir", "improved_test_suites"
    ],
    [
        "python", "agent_runner.py",
        "--modules", "initial_test_suites/queue_example/queue_example.py",
        "--test", "initial_test_suites/queue_example/test_queue_example.py",
        "--semantics", "prompts/prompt_semantic_analysis.txt",
        "--changes_file", "prompts/all_changes.txt",
        "--output_dir", "improved_test_suites"
    ],
    [
        "python", "agent_runner.py",
        "--modules", "initial_test_suites/string_utils_validation/validation.py",
        "--test", "initial_test_suites/string_utils_validation/test_string_utils_validation.py",
        "--semantics", "prompts/prompt_semantic_analysis.txt",
        "--changes_file", "prompts/all_changes.txt",
        "--output_dir", "improved_test_suites"
    ]
]

for i, cmd in enumerate(commands, start=1):
    print(f"Running command {i}...")
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"Command {i} completed successfully.\nOutput:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Command {i} failed.\nError Output:\n{e.stderr}")
