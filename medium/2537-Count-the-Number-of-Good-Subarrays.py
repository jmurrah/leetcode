"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.
"""


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)

        l = output = curr = 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            curr += count[nums[r]] - 1

            while curr >= k:
                output += len(nums) - r
                count[nums[l]] -= 1
                curr -= count[nums[l]]
                l += 1
    
        return output
