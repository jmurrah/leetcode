"""
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 
2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from 
node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from 
that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
"""


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # 1 = safe, 0 = not safe, -1 = visited, -2 = unvisited
        flags = [-2] * len(graph)

        def find_safe(index):
            if flags[index] == 1:
                return True
            if flags[index] == 0:
                return False
            if flags[index] == -1:
                flags[index] = 0
                return False

            flags[index] = -1
            for neighbor in graph[index]:
                if not find_safe(neighbor):
                    flags[index] = -1
                    return False
            
            flags[index] = 1
            return True
        
        for i in range(len(graph)):
            find_safe(i)

        return [i for i, flag in enumerate(flags) if flag == 1]
        
