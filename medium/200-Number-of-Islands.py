"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        found = set()

        def bfs(x, y):
            q = deque()
            q.append((x, y))
            found.add((x, y))

            while q:
                row, col = q.popleft()
                pos = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for xo, yo in pos:
                    r, c = row + xo, col + yo
                    if (r, c) not in found and 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1":
                        q.append((r, c))
                        found.add((r, c))

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in found:
                    bfs(i, j)
                    count += 1
        
        return count
