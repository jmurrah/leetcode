"""
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. 
Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.
"""


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = defaultdict(int), defaultdict(int)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    rows[r] += 1
                    cols[c] += 1
        
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (rows[r] - 1 > 0 or cols[c] - 1 > 0):
                    count += 1
        
        return count
