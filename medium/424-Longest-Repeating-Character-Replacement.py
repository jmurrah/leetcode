"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = longest = 0
        max_key = s[0]

        for r, char in enumerate(s):
            count[char] += 1
            if count[char] > count[max_key]: max_key = char

            while (r-l+1) - count[max_key] > k:
                count[s[l]] -= 1
                if s[l] == max_key: max_key = max(count, key=count.get)
                l += 1

            longest = (max(longest, r-l+1))

        return longest
