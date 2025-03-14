"""
You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

You are given an m x n character matrix, grid, of these different types of cells:

    '*' is your location. There is exactly one '*' cell.
    '#' is a food cell. There may be multiple food cells.
    'O' is free space, and you can travel through these cells.
    'X' is an obstacle, and you cannot travel through these cells.

You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.
"""


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        dq = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "#":
                    dq.appendleft((r, c))

        seen = set()
        level = 0
        while dq:
            for _ in range(len(dq)):
                r, c = dq.pop()
                if grid[r][c] == "*":
                    return level

                for ro, co in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                    row, col = r + ro, c + co
                    if (
                        not (0 <= row < len(grid) and 0 <= col < len(grid[0]))
                        or grid[row][col] in "X#"
                        or (row, col) in seen
                    ):
                        continue
                    seen.add((row, col))
                    dq.appendleft((row, col))

            level += 1

        return -1
