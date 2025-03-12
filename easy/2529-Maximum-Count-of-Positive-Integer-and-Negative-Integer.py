"""
Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

    In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.

Note that 0 is neither positive nor negative.
"""


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negative = 0

        for i, n in enumerate(nums):
            if n < 0:
                negative += 1
            if n > 0:
                return max(negative, len(nums) - i)

        return negative
        
