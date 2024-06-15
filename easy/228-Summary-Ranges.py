"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, 
and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b
"""


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return nums
        output, interval, curr = [], [nums[0]], 0

        for i in range(1, len(nums)):
            if nums[i] - 1 != nums[i-1]:
                interval.append(nums[i-1])
                output.append(interval)
                interval = [nums[i]]

        interval.append(nums[-1])
        output.append(interval)

        for i in range(len(output)):
            start, end = output[i][0], output[i][-1]
            output[i] = f"{start}->{end}" if start != end else f"{start}"

        return output
