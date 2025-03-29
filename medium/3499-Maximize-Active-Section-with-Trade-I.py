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
        s = "1" + s + "1"
        len_s = len(s)
        i = one = zero = 0

        # skip initial 1s
        while i < len_s and s[i] == '1':
            one += 1
            i += 1
        
        # count first block of 0s
        prev = 0
        while i < len_s and s[i] == '0':
            prev += 1
            i += 1
        
        # process the rest of the string
        while i < len_s:
            while i < len_s and s[i] == '1':
                one += 1
                i += 1

            if i == len_s:
                break

            curr = 0
            while i < len_s and s[i] == '0':
                curr += 1
                i += 1
                
            zero = max(zero, prev + curr)
            prev = curr

        return one + zero - 2
