"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        def backtrack(start, current_subset):
            output.append(current_subset.copy())
            for i in range(start, len(nums)):
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()
        
        backtrack(0, [])
        return output
