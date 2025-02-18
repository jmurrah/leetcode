"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
"""


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points_left = set([(x, y) for x, y in points])
        heap = [(0, (points[0][0], points[0][1]))]

        total_cost = 0
        while heap:
            cost, point = heappop(heap)
            if point not in points_left:
                continue

            points_left.remove(point)
            total_cost += cost
            x1, y1 = point

            for x2, y2 in points_left:
                heappush(heap, (abs(x1 - x2) + abs(y1 - y2), (x2, y2)))

        return total_cost
