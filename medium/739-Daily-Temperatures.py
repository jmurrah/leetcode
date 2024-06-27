"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is 
the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which 
this is possible, keep answer[i] == 0 instead.
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, output = [], [0]*len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                output[index] = i - index
            stack.append(i)

        return output
