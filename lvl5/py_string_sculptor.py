def string_sculptor(text: str) -> str:
    res = ""
    i = 0
    for c in text:
        if c.isalpha():
            res += c.upper() if i % 2 else c.lower()
            i += 1
        else:
            res += c
    return res


# Tests
print(string_sculptor("hello"))        # hElLo
print(string_sculptor("Hello World"))  # hElLo WoRlD
print(string_sculptor(" hello "))  # hElLo
print(string_sculptor("abc123def"))    # aBc123DeF
