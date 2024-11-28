"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []

        def backtrack(start, curr):
            if len(curr) == k:
                output.append(curr.copy())
                return

            for i in range(start + 1, n + 1):
                curr.append(i)
                backtrack(i, curr)
                curr.pop()

        backtrack(0, [])
        return output
