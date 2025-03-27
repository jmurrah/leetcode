"""
An element x of an integer array arr of length m is dominant if more than half the elements of arr have a value of x.

You are given a 0-indexed integer array nums of length n with one dominant element.

You can split nums at an index i into two arrays nums[0, ..., i] and nums[i + 1, ..., n - 1], but the split is only valid if:

    0 <= i < n - 1
    nums[0, ..., i], and nums[i + 1, ..., n - 1] have the same dominant element.

Here, nums[i, ..., j] denotes the subarray of nums starting at index i and ending at index j, both ends being inclusive. 
Particularly, if j < i then nums[i, ..., j] denotes an empty subarray.

Return the minimum index of a valid split. If no valid split exists, return -1.
"""


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        right, dr = defaultdict(int), -1
        for num in nums:
            right[num] += 1
            if right[num] > right[dr]:
                dr = num

        lc = 0
        for i, num in enumerate(nums):
            if num == dr:
                lc += 1
                right[dr] -= 1
            if lc > i - lc + 1 and right[dr] > len(nums) - i - 1 - right[dr]:
                return i

        return -1
