"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        curr = max_vowels = sum(1 for letter in s[:k] if letter in vowels)

        for i in range(k, len(s)):
            curr += (s[i] in vowels) - (s[i-k] in vowels)
            max_vowels = max(curr, max_vowels)
        
        return max_vowels
