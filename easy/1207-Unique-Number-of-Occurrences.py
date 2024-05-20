"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
"""


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}

        for i in range(len(arr)):
            if arr[i] not in count:
                count[arr[i]] = 1
            else:
                count[arr[i]] += 1
        
        return len(set(count.values())) == len(count.values())
