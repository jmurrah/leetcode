"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        rows = [[1], [1, 1]]
        for _ in range(numRows - 2):
            row = []
            for j in range(1, len(rows[-1])):
                row.append(rows[-1][j] + rows[-1][j-1])
            rows.append([1] + row + [1])
                
        return rows
