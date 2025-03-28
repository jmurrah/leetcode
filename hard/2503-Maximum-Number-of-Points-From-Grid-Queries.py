"""
You are given an m x n integer matrix grid and an array queries of size k.

Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:

    If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting 
    this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
    Otherwise, you do not get any points, and you end this process.

After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

Return the resulting array answer.
"""


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        answers = {}
        sq = sorted(queries)
        heap, seen = [(grid[0][0], 0, 0)], set([(0, 0)])
        p = i = 0

        while heap:
            q, r, c = heappop(heap)
            while i < len(sq) and q >= sq[i]:
                answers[sq[i]] = p
                i += 1
            if i >= len(sq):
                break
            p += 1
            for ro, co in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                row, col = r + ro, c + co
                if (
                    not (0 <= row < len(grid) and 0 <= col < len(grid[0]))
                    or (row, col) in seen
                ):
                    continue
                seen.add((row, col))
                heappush(heap, (grid[row][col], row, col))

        for j in range(i, len(sq)):
            answers[sq[j]] = p
            
        return [answers[q] for q in queries]
