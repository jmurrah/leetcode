"""
You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:

    Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
    Remove the last character of a string t and give it to the robot. The robot will write this character on paper.

Return the lexicographically smallest string that can be written on the paper.
"""


class Solution:
    def robotWithString(self, s: str) -> str:
        dp = [s[-1]] * len(s) # find smallest to right
        for i in range(len(s)-2, -1, -1):
            dp[i] = s[i] if s[i] < dp[i+1] else dp[i+1]

        stack, output, = [], []
        for i in range(len(s)):
            while stack and dp[i] >= stack[-1]:
                output.append(stack.pop())
            stack.append(s[i])

        while stack:
            output.append(stack.pop())
        
        return "".join(output)
