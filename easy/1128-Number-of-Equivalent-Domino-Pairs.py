"""
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].
"""


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = defaultdict(int)
        for ele in dominoes:
            s = sum(ele)
            if (ele[0], s) in counts:
                counts[(ele[0], s)] += 1
            else:
                counts[(ele[1], s)] += 1
        
        output = 0
        for k, v in counts.items():
            output += v * (v - 1) // 2
        
        return output
