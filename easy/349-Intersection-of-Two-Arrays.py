"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1, s2 = set(nums1), set(nums2)
        output = set()

        for num in s1:
            if num in s2:
                output.add(num)

        return output
