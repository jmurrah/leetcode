"""
You are given an array of integers nums. Return the length of the longest subarray of nums which is either
strictly increasing or strictly decreasing.
"""


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = dec = longest = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i-1]:
                inc = 1
                dec += 1
            else:
                inc = dec = 1
            longest = max(longest, inc, dec)
        
        return longest
