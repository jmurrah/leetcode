"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every 
character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        counter = Counter(t)
        num_missing = len(t)
        min_window_length = float('inf')

        l = r = 0
        while r < len(s):
            if counter[s[r]] > 0:
                num_missing -= 1
            counter[s[r]] -= 1
            r += 1

            while num_missing == 0:
                if (r - l) < min_window_length:
                    min_window_length = r - l
                    substring = s[l:r]

                counter[s[l]] += 1
                if counter[s[l]] > 0:
                    num_missing += 1
                l += 1

        return substring if min_window_length != float('inf') else ""
