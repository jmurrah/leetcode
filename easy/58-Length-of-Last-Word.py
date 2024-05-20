"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
        for i in reversed(range(len(s))):
            if s[i] != " ":
                count += 1
            elif count != 0:
                return count
            else:
                count = 0

            if i == 0:
                return count
