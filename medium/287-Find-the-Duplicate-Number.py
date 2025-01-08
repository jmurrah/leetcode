"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        start = True

        while slow != fast or start:
            start = False
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        new_slow = 0
        while new_slow != slow:
            new_slow = nums[new_slow]
            slow = nums[slow]
        
        return slow
