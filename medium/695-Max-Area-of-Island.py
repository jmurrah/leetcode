"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area, found = 0, set()

        def bfs(x, y):
            q, count = deque(), 1
            q.append((x, y))
            found.add((x, y))

            while q:
                row, col = q.popleft()
                pos = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for xo, yo in pos:
                    r, c = row + xo, col + yo
                    if (r, c) not in found and 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                        count += 1
                        q.append((r, c))
                        found.add((r, c))
            return count

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in found:
                    max_area = max(bfs(i, j), max_area)

        return max_area
