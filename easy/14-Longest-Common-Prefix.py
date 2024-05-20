"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        for i in range(len(strs[0])):
            if strs[0][i] != strs[-1][i]: 
                return strs[0][:i]

        return strs[0]
