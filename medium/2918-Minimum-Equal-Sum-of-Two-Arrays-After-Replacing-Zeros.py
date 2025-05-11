"""
You are given two arrays nums1 and nums2 consisting of positive integers.

You have to replace all the 0's in both arrays with strictly positive integers such that the sum of elements of both arrays becomes equal.

Return the minimum equal sum you can obtain, or -1 if it is impossible.
"""


class Solution:
    def convertAndGetSum(self, nums):
        s, found = 0, False
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = 1
                found = True
            s += nums[i]
        return s, found

    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1, f1 = self.convertAndGetSum(nums1)
        s2, f2 = self.convertAndGetSum(nums2)

        if (not f1 and s2 > s1) or (not f2 and s1 > s2):
            return -1
        
        return max(s1, s2)

        
