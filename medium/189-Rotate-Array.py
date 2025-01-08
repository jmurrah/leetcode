"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""


class Solution:
    def reverse(self, l, r, nums):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        k %= len_nums

        self.reverse(0, len_nums-1, nums)
        self.reverse(0, k-1, nums)
        self.reverse(k, len_nums-1, nums)
