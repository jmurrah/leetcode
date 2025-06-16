"""
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), 
such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.
"""


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        output, c_min = float("-inf"), nums[0]
        for i in range(1, len(nums)):
            if nums[i] > c_min:
                output = max(output, nums[i] - c_min)
            c_min = min(nums[i], c_min)
        
        return output if output != float("-inf") else -1
