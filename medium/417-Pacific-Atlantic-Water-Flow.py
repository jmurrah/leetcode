"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and 
bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] 
represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west 
if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent 
to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) 
to both the Pacific and Atlantic oceans.
"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()

        def search(x, y, s, prev):
            if (x, y) in s or not (0 <= x < len(heights) and 0 <= y < len(heights[0])) or not heights[x][y] >= prev:
                return
            s.add((x, y))
            search(x+1, y, s, heights[x][y])
            search(x, y+1, s, heights[x][y])
            search(x-1, y, s, heights[x][y])
            search(x, y-1, s, heights[x][y])

        for i in range(len(heights)):
            search(i, 0, pacific, heights[i][0])
            search(i, len(heights[0])-1, atlantic, heights[i][len(heights[0])-1])

        for j in range(len(heights[0])):
            search(0, j, pacific, heights[0][j])
            search(len(heights)-1, j, atlantic, heights[len(heights)-1][j])

        return list(pacific & atlantic)

