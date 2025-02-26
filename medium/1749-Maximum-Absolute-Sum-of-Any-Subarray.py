"""
You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

    If x is a negative integer, then abs(x) = -x.
    If x is a non-negative integer, then abs(x) = x.
"""


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        pos = neg = output = 0

        for n in nums:
            pos = pos + n if n + pos > 0 else 0
            neg = neg + n if n + neg < 0 else 0
            output = max(output, abs(pos), abs(neg))
        
        return output
