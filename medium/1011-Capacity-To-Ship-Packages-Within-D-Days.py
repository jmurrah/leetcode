"""
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt 
(in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
"""


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = 1, 500 * len(weights)

        while l <= r:
            m = (l + r) // 2
            i = j = 0
            while i < days and j < len(weights):
                curr = 0
                while j < len(weights) and curr + weights[j] <= m:
                    curr += weights[j]
                    j += 1
                i += 1

            if i <= days and j == len(weights):
                r = m - 1
            else:
                l = m + 1

        return l
