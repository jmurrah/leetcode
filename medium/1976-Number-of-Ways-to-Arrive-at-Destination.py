"""
You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. 
The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes 
timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.
"""


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        adj = defaultdict(list)
        for n1, n2, w in roads:
            adj[n1].append((n2, w))
            adj[n2].append((n1, w))
        
        min_node_cost = [0] + [float("inf")] * (n-1)
        count = [1] + [0] * (n-1)
        heap = [(0, 0)]

        while heap:
            cost, node = heappop(heap)
            if cost > min_node_cost[node]:
                continue
                
            for neighbor, weight in adj[node]:
                new_cost = cost + weight
                if new_cost < min_node_cost[neighbor]:
                    min_node_cost[neighbor] = new_cost
                    count[neighbor] = count[node]
                    heappush(heap, (new_cost, neighbor))
                elif new_cost == min_node_cost[neighbor]:
                    count[neighbor] = (count[neighbor] + count[node]) % MOD
        
        return count[n - 1] % MOD
