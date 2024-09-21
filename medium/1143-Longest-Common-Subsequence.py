"""
Given two strings text1 and text2, return the length of their longest common subsequence. 
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters 
(can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        d = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

        for t1 in range(len(text1)-1, -1, -1):
            for t2 in range(len(text2)-1, -1, -1):
                if text1[t1] == text2[t2]:
                    d[t1][t2] = 1 + d[t1+1][t2+1] 
                else:
                    d[t1][t2] = max(d[t1+1][t2], d[t1][t2+1])
        
        return d[0][0]
