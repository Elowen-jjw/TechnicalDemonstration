## Some Unsuccessful Attempts

I experimented with several rules to improve test structure, but most turned out to be unhelpful.

### Test Splitting
- Split tests if they had many assertions (≥5) or were too long (>60 lines).  

### Code Flattening
- Inlined simple helper calls  
- Simplified nested `if-else` logic

### Assertion Grouping and Formatting
- Grouped assertions based on what they checked

### Test Hygiene
- Replaced hardcoded file paths and URLs with parameters  
- Used standard fixtures like tmp_path and monkeypatch  
- Added type hints for unclear fixture inputs

### Exception Handling
- Replaced `xfail` with `pytest.raises(...)` and added message checks

### Comments 
- Explain non-obvious setup rationale  
- Avoided restating what the code already makes clear

**However, most tests did not get significantly better**:
- Splitting often made things worse. Many tests already focus on a single goal, so breaking them up hurt clarity.
- A lot of tests were already concise and structured.
- Assertions tended to be closely related, so grouping or splitting them didn’t help much.
- Without deeper semantic understanding (e.g., what each assertion means), these edits were mostly cosmetic.


