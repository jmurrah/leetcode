"""
Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 10^9 + 7.
"""


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        num_odd = num_even = curr_sum = count = 0

        for i, n in enumerate(arr):
            curr_sum += n
            if curr_sum % 2 == 1:
                count += num_even + 1
                num_odd += 1
            else:
                count += num_odd
                num_even += 1

        return count % (10 ** 9 + 7)
