"""
You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.

While there is a '*', do the following operation:

    Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.

Return the
resulting string after removing all '*' characters.
"""


class Solution:
    def clearStars(self, s: str) -> str:
        skip, h = set(), []

        for i in range(len(s)):
            if s[i] == "*":
                char, index = heappop(h)
                skip.add(-index)
            else:
                heappush(h, (s[i], -i))
        
        return "".join([c for i, c in enumerate(s) if i not in skip and c != "*"])
