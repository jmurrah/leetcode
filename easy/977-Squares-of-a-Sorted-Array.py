"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, i = 0, len(nums) - 1, len(nums) - 1
        output = [0] * len(nums)

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                output[i] = nums[l] ** 2
                l += 1
            else:
                output[i] = nums[r] ** 2
                r -= 1
            i -= 1
        
        return output
