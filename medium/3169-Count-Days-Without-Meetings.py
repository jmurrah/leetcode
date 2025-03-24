"""
You are given a positive integer days representing the total number of days an employee is available for work 
(starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] 
represents the starting and ending days of meeting i (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.

Note: The meetings may overlap.
"""


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: (x[0], -x[1]))
        output = prev_end = 0

        for start, end in meetings:
            if start > prev_end:
                output += start - prev_end - 1
            if prev_end < end:
                prev_end = end
        
        return output + days - prev_end
