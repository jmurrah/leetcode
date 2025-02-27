"""
A sequence x1, x2, ..., xn is Fibonacci-like if:

    n >= 3
    xi + xi+1 == xi+2 for all i + 2 <= n

Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like 
subsequence of arr. If one does not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without 
changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].
"""


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        mc, dp, nums = 0, {}, set(arr)

        for i, prev in enumerate(arr):
            for curr in arr[i+1:]:
                start = curr - prev
                if start not in nums or start >= prev:
                    continue
                dp[(prev, curr)] = dp.get((start, prev), 2) + 1
                mc = max(mc, dp[(prev, curr)])

        return mc if mc > 2 else 0
