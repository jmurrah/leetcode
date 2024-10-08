"""
There are n mountains in a row, and each mountain has a height. You are given an integer array height where height[i] 
represents the height of mountain i, and an integer threshold.

A mountain is called stable if the mountain just before it (if it exists) has a height strictly greater than threshold. 
Note that mountain 0 is not stable.

Return an array containing the indices of all stable mountains in any order.
"""


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        output = []
        prev = height[0]

        for i, h in enumerate(height[1:]):
            if prev > threshold:
                output.append(i + 1)
            prev = h
        
        return output
