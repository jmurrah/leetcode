"""
You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i]. 
You can divide each pile into any number of sub piles, but you cannot merge two piles together.

You are also given an integer k. You should allocate piles of candies to k children such that each child gets the same 
number of candies. Each child can be allocated candies from only one pile of candies and some piles of candies may go unused.

Return the maximum number of candies each child can get.
"""


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, max(candies)

        while l <= r:
            m = (l + r) // 2
            if sum([n // m for n in candies]) >= k:
                l = m + 1
            else:
                r = m - 1

        return r
