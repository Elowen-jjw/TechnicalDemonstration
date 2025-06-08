## Some Unsuccessful Attempts

I experimented with several rules to improve test structure:

### Test Splitting
- Split tests with ≥5 assertions or >60 lines  

### Code Flattening
- Inlined simple helper calls  
- Simplified nested `if-else` logic

### Assertion Grouping and Formatting
- Grouped assertions by test objective

### Test Hygiene
- Parameterize hardcoded file paths and URLs  
- Use standard fixtures (`tmp_path`, `monkeypatch`)  
- Add type hints to ambiguous fixture inputs  

### Exception Handling
- Replaced `xfail` with `pytest.raises(...)` and added message checks

### Comments 
- Explain non-obvious setup rationale  
- Avoid redundant code descriptions  

**However, most tests did not get significantly better**:
- Over-splitting hurt clarity, as tests naturally focus on single logical goals.  
- Most tests were already concise.  
- Assertions are tightly related, so splitting isn not helpful.  
- Without deeper code semantics understanding, improvements were shallow. 
