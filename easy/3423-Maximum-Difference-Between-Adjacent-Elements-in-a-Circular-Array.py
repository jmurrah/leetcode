"""
Given a circular array nums, find the maximum absolute difference between adjacent elements.

Note: In a circular array, the first and last elements are adjacent.
"""


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max(
            [abs(nums[i] - nums[i - 1]) for i in range(1, len(nums))]
            + [abs(nums[0] - nums[-1])],
        )
