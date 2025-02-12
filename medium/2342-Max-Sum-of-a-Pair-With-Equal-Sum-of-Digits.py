"""
You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.
"""


class Solution:
    def getDigitSum(self, num):
        ds = 0
        while num:
            ds += num % 10
            num //= 10
        return ds

    def maximumSum(self, nums: List[int]) -> int:
        digit_sums, output = {}, -1
        
        for num in nums:
            ds = self.getDigitSum(num)
            if ds in digit_sums:
                output = max(output, num + digit_sums[ds])
                digit_sums[ds] = max(digit_sums[ds], num)
            else:
                digit_sums[ds] = num
        
        return output
