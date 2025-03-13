"""
You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].

For each queries[i]:

    Select a subset of indices within the range [li, ri] in nums.
    Decrement the values at the selected indices by 1.

A Zero Array is an array where all elements are equal to 0.

Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.
"""


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        differences = [0] * (len(nums) + 1)
        for s, e in queries:
            differences[s] -= 1
            differences[e+1] += 1
        
        curr = 0
        for i in range(len(nums)):
            curr += differences[i]
            if nums[i] + curr > 0:
                nums[i] += curr
            else:
                nums[i] = 0
        
        return sum(nums) == 0
