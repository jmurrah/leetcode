"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0

        def search(l, r):
            while 0 <= l and r < len(s) and s[l] == s[r]:
                self.count += 1
                l -= 1
                r += 1
            
        for i in range(len(s)):
            search(i, i)
            search(i, i + 1)
        
        return self.count
