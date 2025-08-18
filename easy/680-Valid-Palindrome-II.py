"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
"""


class Solution:
    def isPalindrome(self, s, l, r):
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return self.isPalindrome(s, l, r-1) or self.isPalindrome(s, l+1, r)
            l += 1
            r -= 1
        return True
