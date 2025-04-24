"""
You are given an array nums consisting of positive integers.

We call a subarray of an array complete if the following condition is satisfied:

    The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.

Return the number of complete subarrays.

A subarray is a contiguous non-empty part of an array.
"""


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        keys = set(nums)
        c = defaultdict(int)
      
        l = output = 0
        for r in range(len(nums)):
            c[nums[r]] += 1
            while c.keys() == keys:
                output += len(nums) - r
                c[nums[l]] -= 1
                if c[nums[l]] == 0:
                    del c[nums[l]]
                l += 1
        
        return output
