"""
You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. 
A mechanic with a rank r can repair n cars in r * n2 minutes.

You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

Return the minimum time taken to repair all the cars.

Note: All the mechanics can repair the cars simultaneously.
"""


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 1, min(ranks) * cars ** 2

        while l <= r:
            m = (l + r) // 2

            count = 0
            for rank in ranks:
                count += floor(sqrt(m / rank))

            if count < cars:
                l = m + 1
            else:
                r = m - 1
        
        return l
