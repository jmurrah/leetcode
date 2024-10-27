"""
Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals 
that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.
"""


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        output = [intervals[0]]
        ps, pe = intervals[0]
        for start, end in intervals[1:]:
            if not ps <= start <= end <= pe:
                output.append([start, end])
                ps, pe = start, end
        
        return len(output)
