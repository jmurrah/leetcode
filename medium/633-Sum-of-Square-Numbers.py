"""
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
"""


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(c ** 0.5)

        while l <= r:
            ans = (l ** 2) + (r ** 2)
            if ans == c:
                return True
            elif ans > c:
                r -= 1
            else:
                l += 1
        
        return False
