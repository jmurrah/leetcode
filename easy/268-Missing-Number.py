"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        
        for n in range(len(nums)):
            if n not in s:
                return n
            
        return len(nums)
