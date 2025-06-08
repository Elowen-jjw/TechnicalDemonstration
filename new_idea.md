## A new idea driven this paper:

Right now, each test transformation is applied individually. The system assumes that all changes are equally safe and will not alter the meaning of the test. However, in real cases, some edits may unintentionally modify the behavior or weaken the semantic purpose of the test.

To address this, I porpose a simple scoring system that checks how risky or complex each transformation is. It has three parts:
1. Ordering by Difficulty
   Plan the changes from easy to hard. Use simple rules or past experience to decide the order.
2. Impact Detection with Code Diff
   For each transformation, automatically compare the test code before and after the change using:
   * AST-level diff
   * Control flow and assertion pattern analysis
   * (Optionally) Token-level edit distance for simpler similarity estimation
   Based on this comparison, we compute an  an _impact score_—such as the number of changed AST nodes, newly added branches, or reordered statements—to measure semantic deviation.
3. Risk Marking Based on Threshold
   If the impact score exceeds a preset threshold, we mark the transformation as risky.

This approach can:
* Help reorder or skip risky transformations in future iterations
* Trigger warnings for manual review
* Serve as feedback to improve prompt design or isolate complex edits
