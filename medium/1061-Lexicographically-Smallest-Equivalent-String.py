"""
You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

    For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.

Equivalent characters follow the usual rules of any equivalence relation:

    Reflexivity: 'a' == 'a'.
    Symmetry: 'a' == 'b' implies 'b' == 'a'.
    Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.

For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of 
baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.
"""


class UnionFind:
    def __init__(self):
        self.p = {i: i for i in range(97, 97 + 26)}
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 < p2:
            self.p[p2] = p1
        else:
            self.p[p1] = p2
    
    def find(self, n):
        if self.p[n] == n:
            return n
        self.p[n] = self.find(self.p[n])
        return self.p[n]
        
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()
        for i in range(len(s1)):
            uf.union(ord(s1[i]), ord(s2[i]))
        
        output = []
        for c in baseStr:
            output.append(chr(uf.find(ord(c))))

        return "".join(output)
