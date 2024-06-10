"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
"""


class Solution:
    def get_dictionary_values(self, string, sentence=True):
        dictionary = defaultdict(list)
        if not sentence: string = string.split()

        for k, v in enumerate(string):
            dictionary[v].append(k)

        return map(tuple, dictionary.values())

    def wordPattern(self, pattern: str, s: str) -> bool:
        return set(self.get_dictionary_values(pattern)) == set(self.get_dictionary_values(s, sentence=False))
