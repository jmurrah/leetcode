"""
You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, 
such that all the 1's in grid lie inside this rectangle.

Return the minimum possible area of the rectangle.
"""


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        x_min = y_min = float("inf")
        x_max = y_max = float("-inf")
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    x_min = min(x_min, j)
                    x_max = max(x_max, j)
                    y_min = min(y_min, i)
                    y_max = max(y_max, i)
        
        return (x_max - x_min + 1) * (y_max - y_min + 1)
