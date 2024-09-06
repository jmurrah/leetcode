"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need 
to remove to make the rest of the intervals non-overlapping.
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[0])
        count = 0
        prevE = intervals[0][1]

        for start, end in intervals[1:]:
            if prevE > start:
                count += 1
                if prevE < end:
                    continue
            prevE = end
        
        return count
