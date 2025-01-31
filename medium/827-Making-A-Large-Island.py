"""
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.
"""


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        islands_size = defaultdict(int)

        def dfs(r, c, island_id):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] != 1:
                return

            islands_size[island_id] += 1
            grid[r][c] = island_id

            for ro, co in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                dfs(r + ro, c + co, island_id)

        island_id = -1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    dfs(r, c, island_id)
                    island_id -= 1
        
        largest_island = 0
        zero_found = False
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    zero_found = True
                    curr, seen = 0, set()
                    for ro, co in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        row, col = r + ro, c + co
                        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])) or grid[row][col] in seen:
                            continue
                        seen.add(grid[row][col])
                        curr += islands_size[grid[row][col]]
                    largest_island = max(largest_island, curr)
        
        return largest_island + 1 if zero_found else len(grid) * len(grid[0])
