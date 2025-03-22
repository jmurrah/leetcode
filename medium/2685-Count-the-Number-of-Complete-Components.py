"""
You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. 
You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.
"""


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        seen = set()
        def dfs(node, group):
            if node in seen:
                return []
            
            seen.add(node)
            group.append(node)
            for neighbor in adj[node]:
                dfs(neighbor, group)
                
            return group
                
        output = 0
        for node in range(n):
            group = dfs(node, [])
            if group and all([len(adj[node]) == len(group) - 1 for node in group]):
                output += 1

        return output

