"""
You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

Each queries[i] represents the following action on nums:

    Decrement the value at each index in the range [li, ri] in nums by at most vali.
    The amount by which each value is decremented can be chosen independently for each index.

A Zero Array is an array with all its elements equal to 0.

Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, 
nums becomes a Zero Array. If no such k exists, return -1.
"""


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        pref = [0] * (len(nums) + 1)
        max_decr = q = 0

        for i, num in enumerate(nums):
            while max_decr + pref[i] < nums[i]:
                if q == len(queries):
                    return -1

                s, e, v = queries[q]
                q += 1

                if e >= i:
                    pref[max(s, i)] += v
                    pref[e+1] -= v

            max_decr += pref[i]

        return q
