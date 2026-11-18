import heapq


def cryptic_sorter(strings: list[str]) -> list[str]:
    def key(s): return (len(s), s.lower(), sum(
        c in "aeiou" for c in s.lower()))
    return heapq.nsmallest(len(strings), strings, key=key)


# Tests
print(cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"]))
print(cryptic_sorter(["aaa", "bbb", "AAA", "BBB"]))
print(cryptic_sorter(["hello", "world", "hi", "test"]))
print(cryptic_sorter(["a", "A", "a"]))  # Equal strings stay in input order
