"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for i in nums:
            if i in s:
                return True
            s.add(i)
        
        return False
