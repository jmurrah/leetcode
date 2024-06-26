"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        c1 = len(nums1)-len(nums2)
        c2 = len(nums2)

        z = len(nums1)-1
        while c1 > 0 and c2 > 0:
            if nums1[c1-1] < nums2[c2-1]:
                nums1[z] = nums2[c2-1]
                c2 -= 1
            else:
                nums1[z] = nums1[c1-1]
                c1 -= 1
            z -= 1
        
        while c2 > 0:
            nums1[z] = nums2[c2-1]
            c2 -= 1
            z -= 1
