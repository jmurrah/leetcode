"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which 
minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        nr, nc = len(grid)-1, len(grid[0])-1
        d = {(nr, nc): grid[nr][nc]}
        
        for i in range(nr-1, -1, -1):
            d[i, nc] = grid[i][nc] + d[(i+1, nc)]

        for j in range(nc-1, -1, -1):
            d[nr, j] = grid[nr][j] + d[(nr, j+1)]

        for i in range(nr-1, -1, -1):
            for j in range(nc-1, -1, -1):
                d[(i, j)] = grid[i][j] + min(d[(i+1, j)], d[(i, j+1)])

        return d[(0, 0)]
