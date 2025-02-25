"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times 
as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is 
the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive 
the signal. If it is impossible for all the n nodes to receive the signal, return -1.
"""


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [float("inf")] * n
        adj = defaultdict(list)
        for src, tar, w in times:
            adj[src-1].append((tar-1, w))

        h, distances[k-1] = [(0, k - 1)], 0
        while h:
            dist, src = heappop(h)
            for tar, w in adj[src]:
                new_dist = dist + w
                if new_dist < distances[tar]:
                    distances[tar] = new_dist
                    heappush(h, (new_dist, tar))

        return max(distances) if float("inf") not in distances else -1
