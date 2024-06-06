"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []

        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1]: 
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                triple = nums[l] + nums[r] + nums[i]
        
                if triple < 0:
                    l += 1
                elif triple > 0:
                    r -= 1
                else:
                    out.append([nums[l], nums[r], nums[i]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return out
