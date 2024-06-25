"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of 
candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []

        def add(i, current_sum, current_list):
            if current_sum > target or i >= len(candidates):
                return
            if current_sum == target:
                output.append(current_list.copy())
                return

            current_list.append(candidates[i])
            add(i, current_sum + candidates[i], current_list)
            current_list.pop()
            add(i+1, current_sum, current_list)

        add(0, 0, [])
        return output
