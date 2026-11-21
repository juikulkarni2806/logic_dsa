from typing import List

def move_zeros(nums: List[int]) -> List[int]:
    insert_pos = 0
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1
    return nums

print("Moved Zeros:", move_zeros([5, 1, 6, 3, 12,0,11,15,0,24,12,0,122,45]))  # Output: [1, 3, 12, 0, 0]