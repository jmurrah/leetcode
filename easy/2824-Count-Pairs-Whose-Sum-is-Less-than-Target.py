"""
Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target. 
"""


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()

        def search(t):
            count = 0
            l, r = 0, len(nums) - 1
            while l < r:
                num = nums[l] + nums[r]
                if num >= t:
                    r -= 1
                else:
                    count += r - l
                    l += 1
            return count
        
        return search(target)
