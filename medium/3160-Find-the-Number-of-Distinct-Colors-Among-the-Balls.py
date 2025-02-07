"""
You are given an integer limit and a 2D array queries of size n x 2.

There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored. For every query in queries that 
is of the form [x, y], you mark ball x with the color y. After each query, you need to find the number of distinct colors among the balls.

Return an array result of length n, where result[i] denotes the number of distinct colors after ith query.

Note that when answering a query, lack of a color will not be considered as a color.
"""


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors, balls, unique = {}, {}, 0

        output = []
        for ball, color in queries:
            if ball in balls:
                prev_color = balls[ball]
                colors[prev_color] -= 1
                if colors[prev_color] == 0:
                    unique -= 1
                    del colors[prev_color]
    
            balls[ball] = color
            if color not in colors:
                colors[color] = 1
                unique += 1
            else:
                colors[color] += 1
                
            output.append(unique)
        
        return output
