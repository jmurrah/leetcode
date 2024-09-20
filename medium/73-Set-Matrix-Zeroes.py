"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        topleft = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        topleft = True
                    matrix[0][j] = 0
            
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
                
        if topleft:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        
