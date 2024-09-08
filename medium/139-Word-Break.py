"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seen = set()

        def search(substr, words):
            if len(substr) == 0:
                return True
            if substr in seen:
                return False
        
            for word in words:
                if len(substr) < len(word):
                    continue
                if substr[:len(word)] == word:
                    if search(substr[len(word):], words):
                        return True
                    seen.add(substr)
            
            return False
                
        return search(s, wordDict)
