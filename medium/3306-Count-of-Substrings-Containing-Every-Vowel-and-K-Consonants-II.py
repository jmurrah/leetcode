"""
You are given a string word and a non-negative integer k.

Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.
"""


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atleast(n):
            vc = defaultdict(int)
            vowels = "aeiou"
            total = l = cc = 0

            for r in range(len(word)):
                if word[r] in vowels:
                    vc[word[r]] += 1
                else:
                    cc += 1

                while cc >= n and len(vc) == 5:
                    total += len(word) - r
                    if word[l] in vowels:
                        vc[word[l]] -= 1
                        if not vc[word[l]]:
                            del vc[word[l]]
                    else:
                        cc -= 1
                    l += 1
    
            return total

        return atleast(k) - atleast(k+1)
