"""
You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d = {}

        def dfs(x, y, count):
            if (
                not (0 <= x < len(grid) and 0 <= y < len(grid[0]))
                or grid[x][y] == 0
                or ((x, y) in d and d[(x, y)] < count)
            ):
                return

            d[(x, y)] = count

            dfs(x+1, y, count + 1)
            dfs(x-1, y, count + 1)
            dfs(x, y+1, count + 1)
            dfs(x, y-1, count + 1)

        all_zeroes, ones = True, set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    dfs(i, j, 0)
                    all_zeroes = False
                if grid[i][j] == 1:
                    all_zeroes = False
                    ones.add((i, j))

        keys = set(d.keys())
        if all_zeroes:
            return 0
        return max(d.values()) if d and not ones - keys else -1
