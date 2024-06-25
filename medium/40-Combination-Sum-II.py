"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []

        def dfs(i, current_sum, current_list):
            if current_sum == target:
                output.append(current_list.copy())
                return
            if current_sum > target or i >= len(candidates):
                return

            current_list.append(candidates[i])
            dfs(i + 1, current_sum + candidates[i], current_list)
            current_list.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, current_sum, current_list)

        dfs(0, 0, [])
        return output
