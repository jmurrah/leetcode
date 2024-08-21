"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robbing(arr):
            if len(arr) == 1:
                return arr[0]

            l, r = -1, 0
            for i in range(len(arr)-3, -1, -1):
                arr[i] += max(arr[l], arr[r]) if r != 0 else arr[l]
                l -= 1
                r -= 1
            
            return max(arr[0], arr[1])

        return max(robbing(nums[1:]), robbing(nums[:len(nums)-1]))
