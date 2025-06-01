"""
You are given two positive integers n and limit.

Return the total number of ways to distribute n candies among 3 children such that no child gets more than limit candies.
"""


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        output = 0
        for i in range(limit+1):
            for j in range(limit+1):
                for k in range(limit+1):
                    output += int(i + j + k == n)
                    
        return output
