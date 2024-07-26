"""
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. 
The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n

        while l <= r:
            row = (l + r) // 2
            num_coins = (row * (row + 1)) // 2

            if num_coins == n:
                return row
            elif num_coins < n:
                l = row + 1
            else:
                r = row - 1
        
        return r
