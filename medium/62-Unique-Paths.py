"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down 
or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""


class Solution:
    def uniquePaths(self, m: int, n: int, i=0, j=0) -> int:
        d = {(m-1, n-1): 1}

        def find_path(x, y):
            if not (x < m and y < n):
                return 0
            if (x, y) in d:
                return d[(x, y)]    
            d[(x, y)] = find_path(x+1, y) + find_path(x, y+1)
            return d[(x, y)]

        return find_path(0, 0)
