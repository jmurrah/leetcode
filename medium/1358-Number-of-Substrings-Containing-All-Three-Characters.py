"""
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = defaultdict(int)
        l = output = 0

        for r in range(len(s)):
            d[s[r]] += 1
            while len(d) == 3:
                output += len(s) - r
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del d[s[l]]
                l += 1
        
        return output
