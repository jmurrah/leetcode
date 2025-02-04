"""
Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. 
Note that a subarray of size 1 is ascending.
"""


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = curr_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                curr_sum = 0
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
