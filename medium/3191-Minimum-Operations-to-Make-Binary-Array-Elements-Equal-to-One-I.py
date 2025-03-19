"""
You are given a binary array nums.

You can do the following operation on the array any number of times (possibly zero):

    Choose any 3 consecutive elements from the array and flip all of them.

Flipping an element means changing its value from 0 to 1, and from 1 to 0.

Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.
"""


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        output = 0
        
        for i in range(len(nums)-2):
            if nums[i] == 0:
                for j in range(3):
                    nums[i+j] ^= 1 
                output += 1
        
        return output if all(nums[-2:]) else -1
