"""
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.
"""


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        output = -1
        for k, v in Counter(arr).items():
            if k == v and v > output:
                output = v
        
        return output
