"""
There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" 
and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.

Given the array answers, return the minimum number of rabbits that could be in the forest.
"""


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = Counter(answers)
        
        output = 0
        for num in set(answers):
            if num == 0:
                output += c[num]
            else:
                output += ceil(c[num] / (num + 1)) * (num + 1)
        
        return output
