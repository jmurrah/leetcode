"""
There is an undirected weighted graph with n vertices labeled from 0 to n - 1.

You are given the integer n and an array edges, where edges[i] = [ui, vi, wi] indicates that there is an edge between vertices ui and vi with a weight of wi.

A walk on a graph is a sequence of vertices and edges. The walk starts and ends with a vertex, and each edge connects the vertex that comes before it and the 
vertex that comes after it. It's important to note that a walk may visit the same edge or vertex more than once.

The cost of a walk starting at node u and ending at node v is defined as the bitwise AND of the weights of the edges traversed during the walk. In other words, 
if the sequence of edge weights encountered during the walk is w0, w1, w2, ..., wk, then the cost is calculated as w0 & w1 & w2 & ... & wk, where & denotes the 
bitwise AND operator.

You are also given a 2D array query, where query[i] = [si, ti]. For each query, you need to find the minimum cost of the walk starting at vertex si and ending 
at vertex ti. If there exists no such walk, the answer is -1.

Return the array answer, where answer[i] denotes the minimum cost of a walk for query i.
"""


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        comp, cv, ci = [-1] * n, [], 0
        def dfs(node):
            nonlocal comp_and
            comp[node] = ci
            for neighbor, weight in adj[node]:
                comp_and &= weight
                if comp[neighbor] == -1:
                    dfs(neighbor)

        for i in range(n):
            if comp[i] == -1:
                comp_and = (1 << 30) - 1
                dfs(i)
                cv.append(comp_and)
                ci += 1

        output = []
        for start, end in query:
            if comp[start] != comp[end]:
                output.append(-1)
            else:
                output.append(cv[comp[start]])
                
        return output
