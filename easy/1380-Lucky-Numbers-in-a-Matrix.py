"""
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
"""


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        columns, output = defaultdict(list), []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                columns[j].append(matrix[i][j])
        
        for i in range(len(matrix)):
            min_ele = min(matrix[i])
            for j in range(len(matrix[0])):
                if min_ele == matrix[i][j] and min_ele == max(columns[j]):
                    output.append(min_ele)
        
        return output
