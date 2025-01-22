"""
You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

    If isWater[i][j] == 0, cell (i, j) is a land cell.
    If isWater[i][j] == 1, cell (i, j) is a water cell.

You must assign each cell a height in a way that follows these rules:

    The height of each cell must be non-negative.
    If the cell is a water cell, its height must be 0.
    Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former 
    is directly north, east, south, or west of the latter (i.e., their sides are touching).

Find an assignment of heights such that the maximum height in the matrix is maximized.

Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.
"""


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        dq = deque()
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    dq.appendleft((i, j))
                    isWater[i][j] = 0
                else:
                    isWater[i][j] = -1

        height = 1
        while dq:
            for _ in range(len(dq)):
                r, c = dq.pop()
                for row, col in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
                    if (
                        0 <= row < len(isWater)
                        and 0 <= col < len(isWater[0])
                        and not isWater[row][col] != -1
                    ):
                        isWater[row][col] = height
                        dq.appendleft((row, col))
            height += 1

        return isWater
