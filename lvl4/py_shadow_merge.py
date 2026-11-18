from heapq import merge


def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    return list(merge(list1, list2))


# Tests
print(shadow_merge([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
print(shadow_merge([1, 2, 3], [4, 5, 6]))  # [1, 2, 3, 4, 5, 6]
print(shadow_merge([1], [2, 3, 4]))        # [1, 2, 3, 4]
print(shadow_merge([], [1, 2]))            # [1, 2]
