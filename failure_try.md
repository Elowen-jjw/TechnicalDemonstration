## Some Unsuccessful Attempts

I tried several rules to improve test structure.

### Test Splitting
- I splitted tests if they had many assertions (≥5) or were too long (>60 lines).   

### Code Flattening
- Inlined simple helper calls  
- Simplified nested `if-else` logic

### Assertion Grouping and Formatting
- Grouped assertions by what they tested 

### Test Hygiene
- Replaced hardcoded file paths and URLs with parameters  
- Used standard fixtures like `tmp_path` and `monkeypatch`  
- Added type hints to unclear fixture inputs

### Exception Handling
- Replaced `xfail` with `pytest.raises(...)` and added message checks

### Comments 
- Why some setups exist
- Avoided repeating what the code already says.

**However, most tests did not get significantly better**:
- Too much splitting actually hurt clarity. Each test often checks one clear goal, so breaking it apart made the logic harder to follow.
- Many tests are short and already well-structured.  
- Assertions are tightly related, so splitting isn not helpful.  
- Without deeper code understanding—like knowing what each assertion really targets—the improvements remain limited.
