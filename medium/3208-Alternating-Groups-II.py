"""
There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

    colors[i] == 0 means that tile i is red.
    colors[i] == 1 means that tile i is blue.

An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one 
has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.
"""


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        l, r, len_c = 0, 1, len(colors)

        count = 0
        while l < len_c:
            if colors[r % len_c] == colors[(r-1) % len_c]:
                l = r
            elif r - l + 1 == k:
                count += 1
                l += 1
            r += 1
        
        return count
        
