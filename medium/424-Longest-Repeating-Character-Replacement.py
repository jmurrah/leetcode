"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = longest = 0
        max_freq = 1

        for r, char in enumerate(s):
            count[char] += 1
            if count[char] > max_freq: max_freq = count[char]

            while (r-l+1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            longest = (max(longest, r-l+1))

        return longest
