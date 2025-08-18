"""
There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

You are given two integer arrays position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

A car fleet is a car or cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

Return the number of car fleets that will arrive at the destination.
"""


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos = [(position[i], speed[i]) for i in range(len(speed))]
        steps = [(target - p[0]) / p[1] for p in sorted(pos)]

        count = 0
        lead = steps[-1]
        for i in range(len(steps)-2, -1, -1):
            if steps[i] > lead:
                count += 1
                lead = steps[i]

        return count + 1
        
