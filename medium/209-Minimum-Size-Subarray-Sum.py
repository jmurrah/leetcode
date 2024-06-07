"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = s = 0
        m = float("inf")

        for r in range(len(nums)):
            s += nums[r]
            
            while s >= target:
                m = min(r - l + 1, m)
                s -= nums[l]
                l += 1
        
        return m if m != float("inf") else 0
