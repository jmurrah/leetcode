"""
You are given an array nums consisting of positive integers.

We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

Return the length of the longest nice subarray.

A subarray is a contiguous part of an array.

Note that subarrays of length 1 are always considered nice.
"""


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = curr = output = 0

        for r in range(len(nums)):
            while curr & nums[r] != 0:
                curr ^= nums[l]
                l += 1
            curr ^= nums[r]
            output = max(output, r - l + 1)
        
        return output
