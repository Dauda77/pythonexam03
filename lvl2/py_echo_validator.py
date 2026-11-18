def echo_validator(text: str) -> bool:
    s = "".join(c.lower() for c in text if c.isalpha())
    return s != "" and s == s[::-1]


# Tests
print(echo_validator("racecar"))                  # True
print(echo_validator("A man a plan a canal Panama"))  # True
print(echo_validator("race a car"))               # False
print(echo_validator("Hello, World!"))             # False
print(echo_validator(""))                          # True
