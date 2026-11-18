def pattern_tracker(text: str) -> int:
    return sum(a.isdigit() and b.isdigit() and int(b) == int(a) + 1
               for a, b in zip(text, text[1:]))


# Tests
print(pattern_tracker("123"))          # 2
print(pattern_tracker("12a34"))        # 2
print(pattern_tracker("987654321"))    # 0
print(pattern_tracker("7890"))         # 2
print(pattern_tracker("a12b23c"))      # 2
print(pattern_tracker(""))             # 0
