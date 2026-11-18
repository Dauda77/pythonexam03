def hidenp(small: str, big: str) -> bool:
    it = iter(big)
    return all(c in it for c in small)


# Tests
print(hidenp("abc", "a1b2c3"))  # True
print(hidenp("ace", "abcde"))  # True
print(hidenp("aec", "abcde"))  # False
print(hidenp("", "abc"))       # True
print(hidenp("abc", "ab"))     # False
print(hidenp("ABC", "abc"))    # False
