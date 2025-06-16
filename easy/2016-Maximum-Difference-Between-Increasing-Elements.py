"""
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), 
such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.
"""


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        before = [float("inf")] * (len(nums) + 1)
        after = [float("-inf")] * (len(nums) + 1)

        for i in range(1, len(nums)+1):
            before[i] = nums[i-1] if nums[i-1] < before[i-1] else before[i-1]
        
        for i in range(len(nums)-1, -1, -1):
            after[i] = nums[i] if nums[i] > after[i+1] else after[i+1]

        out = max([after[i] - before[i+1] for i in range(len(nums))])
        return out if out != 0 else -1
      
