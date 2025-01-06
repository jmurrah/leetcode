"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

    For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations 
of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows 
it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

    For example, the next permutation of arr = [1,2,3] is [1,3,2].
    Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
    While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
"""


class Solution:

    def reverse(self, start, nums):
        left = start
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        idx_to_swap = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                idx_to_swap = i
                break
            
        if idx_to_swap == -1:
            self.reverse(0, nums)
            return
        
        target_num = nums[idx_to_swap]
        next_idx = -1
        for i in range(len(nums)-1, idx_to_swap, -1):
            if nums[i] > target_num:
                next_idx = i
                break
        
        nums[idx_to_swap], nums[next_idx] = nums[next_idx], nums[idx_to_swap]
        self.reverse(idx_to_swap + 1, nums)
