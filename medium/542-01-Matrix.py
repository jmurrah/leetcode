"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
"""


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque([])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    mat[i][j] = float("inf")
                else:
                    q.appendleft((i, j, 0))
        
        while q:
            r, c, count = q.pop()
            offsets = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for ro, co in offsets:
                row, col = r + ro, c + co
                if not (0 <= row < len(mat) and 0 <= col < len(mat[0])):
                    continue
                if count < mat[row][col]:
                    mat[row][col] = count + 1
                    q.appendleft((row, col, count + 1))

        return mat
        
