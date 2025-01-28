"""
You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

    A land cell if grid[r][c] = 0, or
    A water cell containing grid[r][c] fish, if grid[r][c] > 0.

A fisher can start at any water cell (r, c) and can do the following operations any number of times:

    Catch all the fish at cell (r, c), or
    Move to any adjacent water cell.

Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.
"""


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] == 0:
                return 0
            
            curr = grid[r][c]
            grid[r][c] = 0

            for ro, co in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                curr += dfs(r + ro, c + co)

            return curr

        output = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    output = max(output, dfs(r, c))
        
        return output
