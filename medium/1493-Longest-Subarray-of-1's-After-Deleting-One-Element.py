"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
"""


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = c = m = z = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                z += 1
            c += 1

            if z > 1:
                if nums[l] == 0:
                    z -= 1
                l += 1
                c -= 1
            else:
                m = max(c, m)
        
        return m-1
