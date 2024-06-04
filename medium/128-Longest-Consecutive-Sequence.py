"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s, m = set(nums), 0

        for i in s:
            count = 1
            if i-1 not in s:
                while i + count in s:
                    count += 1
                m = max(count, m)
        
        return m
