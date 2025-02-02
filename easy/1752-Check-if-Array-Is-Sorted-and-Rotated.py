"""
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.
"""


class Solution:
    def check(self, nums: List[int]) -> bool:
        is_rotated = False

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if is_rotated:
                    return False
                is_rotated = True
        
        return nums[0] >= nums[-1] if is_rotated else True
