"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.
"""


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)

        output = []
        for num in arr2:
            output.extend([num] * count[num])
            del count[num]
        
        keys = sorted(count.keys())
        for k in keys:
            output.extend([k] * count[k])

        return output
        
