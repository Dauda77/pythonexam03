from string import ascii_lowercase as a, ascii_uppercase as A


def whisper_cipher(text: str, shift: int) -> str:
    s = shift % 26
    return text.translate(str.maketrans(a + A, a[s:] + a[:s] + A[s:] + A[:s]))


# Tests
print(whisper_cipher("hello", 3))       # khoor
print(whisper_cipher("Hello World!", 1))  # Ifmmp Xpsme!
print(whisper_cipher("xyz", 3))         # abc
print(whisper_cipher("ABC123def", 5))   # FGH123ijk
print(whisper_cipher("abc", -1))        # zab
print(whisper_cipher("abc", 26))        # abc
