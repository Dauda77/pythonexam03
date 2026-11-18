def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr:
        return []
    k %= len(arr)
    return arr[-k:] + arr[:-k] if k else arr[:]


# Tests
print(twist_sequence([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
print(twist_sequence([1, 2, 3], 1))        # [3, 1, 2]
print(twist_sequence([1, 2, 3, 4], 0))     # [1, 2, 3, 4]
print(twist_sequence([1, 2, 3], 5))        # [2, 3, 1]
print(twist_sequence([], 2))               # []
