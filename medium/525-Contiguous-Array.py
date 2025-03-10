"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: -1}
        pref_sum = output = 0

        for i, num in enumerate(nums):
            pref_sum += 1 if num else -1
            if pref_sum in d:
                output = max(output, i - d[pref_sum])
            else:
                d[pref_sum] = i

        return output
