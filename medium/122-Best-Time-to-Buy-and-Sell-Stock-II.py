"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = l = r = 0

        for r in range(len(prices)):
            if prices[r] > prices[l]:
                total += (prices[r] - prices[l])
                l = r
            while prices[l] > prices[r] and l <= r:
                l += 1
            
        return total
