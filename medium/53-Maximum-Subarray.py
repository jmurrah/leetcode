"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = m = nums[0]

        for num in nums[1:]:
            s = max(num, num + s)
            m = max(s, m)

        return m
