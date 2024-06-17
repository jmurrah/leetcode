"""
Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.
"""


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s): return False

        count, num_odds = Counter(s), 0
        for value in count.values():
            if value % 2 == 1:
                num_odds += 1
            if num_odds > k:
                return False

        return True
