"""
There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.
"""


class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, node):
        if node == self.parents[node]:
            return node
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 != p2:
            if self.size[p1] >= self.size[p2]:
                self.parents[p2] = self.parents[p1]
                self.size[p1] += self.size[p2]
            else:
                self.parents[p1] = self.parents[p2]
                self.size[p2] += self.size[p1]


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for n1, n2 in edges:
            uf.union(n1, n2)
        
        for i in range(n):
            uf.find(i)
            
        return len(set(uf.parents))
        
