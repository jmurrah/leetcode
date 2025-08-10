"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need 
to remove to make the rest of the intervals non-overlapping.
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        pe = intervals[0][1]

        output = 0
        for cs, ce in intervals[1:]:
            if cs < pe:
                output += 1
                pe = min(pe, ce)
            else:
                pe = ce
            
        return output
        
