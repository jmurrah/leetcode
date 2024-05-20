"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        vowels = "aeiouAEIOU"

        rs = list(s)
        while l < r:
            if rs[l] not in vowels:
                l += 1
            if rs[r] not in vowels:
                r -= 1
            if rs[l] in vowels and rs[r] in vowels:
                rs[l], rs[r] = rs[r], rs[l]
                l += 1
                r -= 1
            
        return "".join(rs)
