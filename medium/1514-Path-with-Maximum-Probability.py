"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] 
is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return 
its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer 
by at most 1e-5.
"""


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        distances = [-1] * n
        adj = defaultdict(list)
        for i, nodes in enumerate(edges):
            n1, n2 = nodes
            adj[n1].append((succProb[i], n2))
            adj[n2].append((succProb[i], n1))
    
        h = [(-1, start_node)]
        while h:
            dist, node = heappop(h)
            for w, nn in adj[node]:
                new_dist = dist * -w
                if new_dist > distances[nn]:
                    distances[nn] = new_dist
                    heappush(h, (-new_dist, nn))
        
        return distances[end_node] if distances[end_node] != -1 else 0
