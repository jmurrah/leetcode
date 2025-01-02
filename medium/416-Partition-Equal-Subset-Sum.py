"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both 
subsets is equal or false otherwise.
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total / 2
        possible_sums = set()

        for i in range(len(nums)-1, -1, -1):
            for num in list(possible_sums):
                possible_sums.add(num + nums[i])

            possible_sums.add(nums[i])
            
            if target in possible_sums:
                return True
        
        return False
