"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array 
represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        g = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= g:
                g = i
        
        return g == 0
