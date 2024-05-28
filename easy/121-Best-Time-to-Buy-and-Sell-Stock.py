class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        m = 0
        
        while r < len(prices):
            s = prices[r] - prices[l]
            if s >= 0:
                m = max(s, m)
            else:
                l = r
            r += 1
        
        return m
