def anagram(s1: str, s2: str) -> bool:
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())


# Tests
print(anagram("listen", "silent"))       # True
print(anagram("Triangle", "Integral"))   # True
print(anagram("Dormitory", "Dirty Room"))  # True
print(anagram("hello", "world"))         # False
print(anagram("aabb", "abab"))            # True
print(anagram("abc", "ab"))               # False
