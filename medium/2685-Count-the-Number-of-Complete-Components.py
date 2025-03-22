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
        indegree = defaultdict(int)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            indegree[n1] += 1
            indegree[n2] += 1

        seen = set()
        def bfs(node):
            if node in seen:
                return []

            group = set([node])
            seen.add(node)

            dq = deque([node])
            while dq:
                node = dq.pop()
                for neighbor in adj[node]:
                    if neighbor not in group:
                        seen.add(neighbor)
                        group.add(neighbor)
                        dq.appendleft(neighbor)
            
            return list(group)
                
        groups = []
        for node in range(n):
            group = bfs(node)
            if group:
                groups.append(group)

        output = 0
        for group in groups:
            output += int(all([indegree[node] == len(group) - 1 for node in group]))

        return output
