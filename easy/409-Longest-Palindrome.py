"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest
palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = set()

        for c in s:
            if c not in odd:
                odd.add(c)
            else:
                odd.remove(c)
        
        return len(s) if not odd else len(s) - len(odd) + 1
