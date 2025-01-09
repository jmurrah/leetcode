"""
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).
"""


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        next_values = [(matrix[0][0], 0, 0)] # val, row, col
        heapq.heapify(next_values)

        count = 0
        while True:
            count += 1
            val, row, col = heapq.heappop(next_values)
            if count == k:
                return val
            
            if col == 0 and 0 <= row + 1 < len(matrix):
                heapq.heappush(next_values, (matrix[row+1][col], row+1, col))

            if col + 1 < len(matrix[0]):
                heapq.heappush(next_values, (matrix[row][col+1], row, col+1))
