"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there 
is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. 
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
Determine the perimeter of the island.
"""


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        seen = set()

        def dfs(r, c):
            if (r, c) in seen:
                return 0
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                seen.add((r, c))
                return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            return 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)
