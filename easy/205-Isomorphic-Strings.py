"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st, ts = {}, {}

        for i in range(len(s)):
            if (s[i] in st and st[s[i]] != t[i]) or (t[i] in ts and ts[t[i]] != s[i]):
                return False

            st[s[i]] = t[i]
            ts[t[i]] = s[i]
        
        return True
