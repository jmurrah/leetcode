"""
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty 
substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones 
in the right substring.
"""


class Solution:
    def maxScore(self, s: str) -> int:
        left = 0 if s[0] == "1" else 1
        right = sum([1 for n in s[1:] if n == "1"])
        output = left + right

        for n in s[1:-1]:
            if n == "0":
                left += 1
            if n == "1":
                right -= 1
            output = max(output, left + right)
        
        return output
