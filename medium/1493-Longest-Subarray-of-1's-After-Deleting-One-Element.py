"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
"""


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        zeroes = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeroes += 1

            if zeroes > 1:
                if nums[l] == 0: zeroes -= 1
                l += 1
            else:
                longest = max(longest, r-l)
        
        return longest if zeroes != 0 else len(nums)-1
