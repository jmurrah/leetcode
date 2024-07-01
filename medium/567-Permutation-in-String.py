"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1_count, window_count = Counter(s1), defaultdict(int)
        for i in range(len(s2)):
            if i - len(s1) >= 0:
                if window_count[s2[i-len(s1)]] == 1:
                    del window_count[s2[i-len(s1)]]
                else:
                    window_count[s2[i-len(s1)]] -= 1
            window_count[s2[i]] += 1

            if window_count == s1_count:
                return True
        
        return False
