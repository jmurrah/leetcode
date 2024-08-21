"""
Given a string s, return the longest palindromic substring in s.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.longest = ""

        def search(l, r):
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if len(s[l+1:r]) > len(self.longest):
                self.longest = s[l+1:r]
        
        for i in range(len(s)):
            search(i, i)
            search(i, i + 1)
        
        return self.longest
