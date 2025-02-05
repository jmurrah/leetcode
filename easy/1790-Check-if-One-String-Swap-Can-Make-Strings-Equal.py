"""
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True

        l, r = 0, len(s1) - 1
        while l < len(s1) and s1[l] == s2[l]:
            l += 1
        while 0 <= r and s1[r] == s2[r]:
            r -= 1

        return s1[l] == s2[r] and s1[r] == s2[l] and l < r and s1[l+1:r] == s2[l+1:r]
