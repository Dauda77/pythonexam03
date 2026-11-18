def bracket_validator(s: str) -> bool:
    s = "".join(c for c in s if c in "()[]{}")
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
    return s == ""



print(bracket_validator("()"))      # True
print(bracket_validator("()[]{}"))  # True
print(bracket_validator("(]"))      # False
print(bracket_validator("([)]"))    # False
print(bracket_validator("{[]}"))    # True
print(bracket_validator("((("))     # False
print(bracket_validator("]"))       # False
print(bracket_validator(""))        # True