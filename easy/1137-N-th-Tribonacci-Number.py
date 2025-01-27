"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        seen = {}

        def helper(num):
            if num == 0:
                return 0
            if num <= 2:
                return 1
            if num in seen:
                return seen[num]

            seen[num] = helper(num - 3) + helper(num - 2) + helper(num - 1)
            return seen[num]
        
        return helper(n)
