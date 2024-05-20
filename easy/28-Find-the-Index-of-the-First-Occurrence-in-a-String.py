"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


class Solution(object):
    def strStr(self, haystack, needle):
        if len(haystack) < len(needle):
            return -1
    
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
              
        return -1
