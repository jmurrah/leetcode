"""
You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the score of s.
"""


class Solution:
    def scoreOfString(self, s: str) -> int:
        total, prev = 0, s[0]

        for char in s[1:]:
            total += abs(ord(char) - ord(prev))
            prev = char
        
        return total
