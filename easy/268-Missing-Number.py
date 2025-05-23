"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = len(nums)
        for i, num in enumerate(nums):
            xor ^= i ^ num
        return xor 
