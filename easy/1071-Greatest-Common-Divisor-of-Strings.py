"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        small, large = (str1, str2) if len(str1) < len(str2) else (str2, str1)

        for i in range(len(small), 0, -1):
            if len(large) % i == 0 and small[:i]*(len(small) // i) == small and small[:i]*(len(large) // i) == large:
                return small[:i]
        
        return ""
