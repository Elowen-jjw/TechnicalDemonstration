## A new idea driven this paper:

Right now, each test transformation is applied one by one. The system assumes all changes are equally safe and will not break the test’s meaning. But in real cases, some edits may change the test behavior or remove its original intent.
To solve this, I suggest a simple scoring system that checks how risky or complex each transformation is. This system has three parts:
1. Ordering by Difficulty: Plan the changes from easy to hard. Use simple rules or past experience to decide the order.
2. Impact Detection with Code Diff: For each transformation, automatically compare the test code before and after the change using:
   * AST-level diff (e.g., RedBaron, astdiff, difflib + ast.parse)
   * Control flow and assertion pattern comparison
   * (Optionally) Token-level edit distance for simpler similarity estimation
   We can define an “impact score” (e.g., # of changed nodes, new branches, reordered statements) to quantify the semantic shift.
4. Marking Risk with a Threshold: If the impact score is too high (based on a preset threshold), mark the change as risky.

This can help:
* Reorder or skip certain steps in future iterations;
* Provide user alerts for manual review;
* Serve as feedback to fine-tune prompts or split complex edits.
