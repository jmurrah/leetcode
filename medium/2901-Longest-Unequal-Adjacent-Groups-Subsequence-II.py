"""
You are given a string array words, and an array groups, both arrays having length n.

The hamming distance between two strings of equal length is the number of positions at which the corresponding characters are different.

You need to select the longest

from an array of indices [0, 1, ..., n - 1], such that for the subsequence denoted as [i0, i1, ..., ik-1] having length k, the following holds:

    For adjacent indices in the subsequence, their corresponding groups are unequal, i.e., groups[ij] != groups[ij+1], for each j where 0 < j + 1 < k.
    words[ij] and words[ij+1] are equal in length, and the hamming distance between them is 1, where 0 < j + 1 < k, for all indices in the subsequence.

Return a string array containing the words corresponding to the indices (in order) in the selected subsequence. If there are multiple answers, return any of them.

Note: strings in words may be unequal in length.
"""


class Solution:
    def getHammingDistance(self, w1, w2):
        return sum(int(w1[i] != w2[i]) for i in range(len(w1)))

    def getLongestGroupSubsequence(self, word_group, words, groups):
        m = len(word_group)
        dp = [1] * m
        next_idx = [-1] * m

        for p in range(m - 1, -1, -1):
            i = word_group[p]
            for q in range(p + 1, m):
                j = word_group[q]
                if (
                    self.getHammingDistance(words[i], words[j]) == 1
                    and groups[i] != groups[j]
                ):
                    if dp[q] + 1 > dp[p]:
                        dp[p] = dp[q] + 1
                        next_idx[p] = q

        if m == 0:
            return []

        best_start = max(range(m), key=lambda x: dp[x])
        seq = []
        p = best_start
        while p != -1:
            seq.append(word_group[p])
            p = next_idx[p]

        return seq

    def getWordsInLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:
        word_groups = defaultdict(list)
        for i, word in enumerate(words):
            word_groups[len(word)].append(i)

        output = []
        for word_group in word_groups.values():
            curr = self.getLongestGroupSubsequence(word_group, words, groups)
            if len(curr) > len(output):
                output = curr

        return [words[i] for i in output]
