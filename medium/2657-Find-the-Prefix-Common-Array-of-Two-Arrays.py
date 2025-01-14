"""
You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.
"""


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set_a, set_b, output = set(), set(), []

        curr = 0
        for i in range(len(A)):
            set_a.add(A[i])
            set_b.add(B[i])

            if A[i] in set_b:
                curr += 1
            if A[i] != B[i] and B[i] in set_a:
                curr += 1
            
            output.append(curr)

        return output
