"""
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.
"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ")":
                reverse = []
                while stack[-1] != "(":
                    reverse.append(stack.pop())
                stack.pop()
                stack.extend(reverse)
            else:
                stack.append(char)
        
        return "".join(stack)
