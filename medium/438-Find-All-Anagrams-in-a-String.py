"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        
        l, window_size = 0, len(p)
        current_count, correct_count = defaultdict(int), Counter(p)

        for i in range(window_size):
            if s[i] in correct_count:
                current_count[s[i]] += 1

        output = []
        if current_count == correct_count:
            output.append(0)

        for r in range(window_size, len(s)):
            if s[l] in correct_count:
                current_count[s[l]] -= 1
            if s[r] in correct_count:
                current_count[s[r]] += 1
            l += 1

            if current_count == correct_count:
                output.append(l)

        return output
