"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. 
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The 
graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge 
between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, 
return the answer that occurs last in the input.
"""


class UnionFind:
    def __init__(self, n: int):
        self.parents = {i: i for i in range(1, n+1)}

    def union(self, n1: int, n2: int):
        f1, f2 = self.find(n1), self.find(n2)
        self.parents[f2] = self.parents[f1]
    
    def find(self, node: int):
        if self.parents[node] == node:
            return node
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for n1, n2 in edges:
            f1, f2 = uf.find(n1), uf.find(n2)
            if f1 == f2:
                return [n1, n2]
            uf.union(f1, f2)
