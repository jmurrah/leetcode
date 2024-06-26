"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
"""


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = -1

        for i in range(len(arr)-1, -1, -1):
            if arr[i] > m:
                arr[i], m = m, arr[i]
            else:
                arr[i] = m
        
        return arr
