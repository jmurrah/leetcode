"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return sorted(set(nums), key=nums.count)[::-1][:k]
