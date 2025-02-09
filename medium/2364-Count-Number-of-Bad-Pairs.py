"""
You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums.
"""


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        pairs = defaultdict(int)
        for i in range(len(nums)):
            pairs[nums[i] - i] += 1
        
        good_count = 0
        for count in pairs.values():
            good_count += count * (count - 1) // 2

        return comb(len(nums), 2) - good_count
