"""
Given an integer array nums, return the number of subarrays of length 3 such that the sum of the first and third numbers equals exactly half of the second number.
"""


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        output = 0
        for i in range(2, len(nums)):
            if nums[i-2] + nums[i] == nums[i-1] / 2:
                output += 1
        
        return output
        
