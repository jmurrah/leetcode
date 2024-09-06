"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        output = max(nums)
        cMin = cMax = 1

        for num in nums:
            temp = cMax * num
            cMax = max(temp, num * cMin, num)
            cMin = min(temp, num * cMin, num)
            output = max(output, cMax)

        return output
