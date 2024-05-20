"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
"""


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        my_dict = defaultdict(int)
        count = 0

        for row in grid:
            my_dict[str(row)] += 1
        
        for i in range(len(grid)):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            count += my_dict[str(col)]
            
        return count
