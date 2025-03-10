"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

    For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.

A subarray is a contiguous part of an array.
"""


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atleast(n):
            nc = defaultdict(int)
            l = total = 0

            for r in range(len(nums)):
                nc[nums[r]] += 1
                while len(nc) >= n:
                    total += len(nums) - r
                    nc[nums[l]] -= 1
                    if nc[nums[l]] == 0:
                        del nc[nums[l]]
                    l += 1

            return total
        
        return atleast(k) - atleast(k+1)
