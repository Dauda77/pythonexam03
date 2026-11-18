def string_permutation_checker(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)


# Tests
print(string_permutation_checker("abc", "bca"))       # True
print(string_permutation_checker("abc", "def"))       # False
print(string_permutation_checker("listen", "silent"))  # True
print(string_permutation_checker("", ""))             # True
print(string_permutation_checker("a b", "ba "))       # True
print(string_permutation_checker("Abc", "abc"))       # False
