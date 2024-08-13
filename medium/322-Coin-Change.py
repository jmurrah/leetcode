"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d = [amount + 1] * (amount + 1)
        d[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                d[i] = min(d[i], d[i - coin] + 1)
        
        return d[amount] if d[amount] != amount + 1 else -1
