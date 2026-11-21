from typing import List

def second_largest(arr: List[int]) -> int:
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else -1

print("Second Largest:", second_largest([12, 35, 1, 10, 43, 1]))  # Output: 34