"""
You are given a binary string s of length n, where:

    '1' represents an active section.
    '0' represents an inactive section.

You can perform at most one trade to maximize the number of active sections in s. In a trade, you:

    Convert a contiguous block of '1's that is surrounded by '0's to all '0's.
    Afterward, convert a contiguous block of '0's that is surrounded by '1's to all '1's.

Return the maximum number of active sections in s after making the optimal trade.

Note: Treat s as if it is augmented with a '1' at both ends, forming t = '1' + s + '1'. The augmented '1's do not contribute to the final count.
"""


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        count = s.count("1")
        best = prev = curr = 0

        s += "1"
        for i in range(len(s)):
            if s[i] == "0":
                curr += 1
            else:
                if prev != 0 and curr != 0:
                    best = max(best, prev + curr)
                if curr != 0:
                    prev = curr
                curr = 0

        return best + count
