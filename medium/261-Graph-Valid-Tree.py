"""
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that 
there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.
"""


class UnionFind:

    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, index: int) -> int:
        if self.parents[index] == index:
            return index

        self.parents[index] = self.find(self.parents[index])
        return self.parents[index]

    def union(self, idx1: int, idx2: int) -> None:
        rep1, rep2 = self.find(idx1), self.find(idx2)
        if rep1 == rep2:
            return False
        
        if self.size[rep1] >= self.size[rep2]:
            self.size[rep1] += self.size[rep2]
            self.parents[rep2] = self.parents[rep1]
        else:
            self.size[rep2] += self.size[rep1]
            self.parents[rep1] = self.parents[rep2]

        return True


class Solution:

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 != len(edges):
            return False

        uf = UnionFind(n)
        for n1, n2 in edges:
            if not uf.union(n1, n2):
                return False

        return True
