"""
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.
"""


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        i, j = m, n
        lcs = []
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                lcs.append(str1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        lcs.reverse()
        
        res = []
        i = j = 0
        for c in lcs:
            while str1[i] != c:
                res.append(str1[i])
                i += 1
            while str2[j] != c:
                res.append(str2[j])
                j += 1

            res.append(c)
            i += 1
            j += 1

        res.append(str1[i:])
        res.append(str2[j:])
        return "".join(res)
