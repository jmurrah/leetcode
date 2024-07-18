"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the 
non-overlapping intervals that cover all the intervals in the input.
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        output, overlap = [], intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= overlap[-1] and overlap[-1] < interval[-1]:
                overlap[-1] = interval[-1]
            elif interval[0] > overlap[-1]:
                output.append(overlap)
                overlap = interval
        
        output.append(overlap)
        return output
