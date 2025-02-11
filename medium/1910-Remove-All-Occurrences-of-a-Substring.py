"""
Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:

    Find the leftmost occurrence of the substring part and remove it from s.

Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.
"""


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        part, stack = list(part), []
        len_p = len(part)
        
        for i in range(len(s)):
            stack.append(s[i])
            len_s = len(stack)

            if len_s >= len_p and stack[len_s - len_p:] == part:
                for _ in range(len_p):
                    stack.pop()

        return "".join(stack)
        
