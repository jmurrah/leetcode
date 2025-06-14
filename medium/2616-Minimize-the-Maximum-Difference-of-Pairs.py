"""
You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum 
difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where 
|x| represents the absolute value of x.

Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.
"""


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        def find_pair_count(threshold):
            count = i = 0
            while i < len(nums)-1:
                if nums[i+1] - nums[i] <= threshold:
                    count += 1
                    i += 1
                i += 1
            return count

        l, r = 0, nums[-1] - nums[0]
        while l < r:
            m = (l + r) // 2
            if find_pair_count(m) >= p:
                r = m
            else:
                l = m + 1
        
        return l
