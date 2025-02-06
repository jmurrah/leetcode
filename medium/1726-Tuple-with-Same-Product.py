"""
Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.
"""


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count_prods = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                count_prods[nums[i] * nums[j]] += 1
        
        return 8 * sum(v * (v - 1) // 2 for v in count_prods.values())
