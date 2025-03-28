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
        points = defaultdict(int)
        dq, fringe, seen = deque([(grid[0][0], 0, 0)]), [], set([(0, 0)])
        prev_q = p = 0

        while dq or fringe:
            if dq:
                q, r, c = dq.popleft()
                prev_q = max(prev_q, q)
                p += 1
                points[q] = p
            else:
                q, r, c = heappop(fringe)
                dq.append((q, r, c))
                while fringe and fringe[0][0] == q:
                    dq.append(heappop(fringe))
                for i in range(prev_q, q):
                    points[i] = p
                continue

            for ro, co in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                row, col = r + ro, c + co
                if (
                    not (0 <= row < len(grid) and 0 <= col < len(grid[0]))
                    or (row, col) in seen
                ):
                    continue
                seen.add((row, col))
                if grid[row][col] <= q:
                    dq.append((q, row, col))
                else:
                    heappush(fringe, (grid[row][col], row, col))

        for i in range(prev_q, max(queries)):
            points[i] = p
            
        return [points[q-1] for q in queries]
