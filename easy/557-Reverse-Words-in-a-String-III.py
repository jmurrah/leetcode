"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        n = []
        for i in s.split():
            n.append(i[::-1])

        return " ".join(n)
