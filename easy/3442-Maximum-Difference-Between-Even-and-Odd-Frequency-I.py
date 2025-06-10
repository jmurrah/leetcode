"""
You are given a string s consisting of lowercase English letters.

Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2 in the string such that:

    a1 has an odd frequency in the string.
    a2 has an even frequency in the string.

Return this maximum difference.
"""


class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd, max_even = 0, float("inf")
        c = Counter(s)
        
        for k, v in c.items():
            if v % 2 == 1:
                max_odd = max(max_odd, v)
            else:
                max_even = min(max_even, v)
        
        return max_odd - max_even
