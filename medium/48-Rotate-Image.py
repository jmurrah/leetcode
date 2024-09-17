"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r-l):
                topLeft = matrix[l][i+l]
                matrix[l][i+l] = matrix[r-i][l]
                matrix[r-i][l] = matrix[r][r-i]
                matrix[r][r-i] = matrix[l+i][r]
                matrix[l+i][r] = topLeft
            l += 1
            r -= 1
