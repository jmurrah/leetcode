"""
You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. 
You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], 
representing a rectangle on the grid. Each rectangle is defined as follows:

    (startx, starty): The bottom-left corner of the rectangle.
    (endx, endy): The top-right corner of the rectangle.

Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two 
vertical cuts on the grid such that:

    Each of the three resulting sections formed by the cuts contains at least one rectangle.
    Every rectangle belongs to exactly one section.

Return true if such cuts can be made; otherwise, return false.
"""


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def checkValid(si, ei):
            count, prev_end = 0, 1
            for rectangle in rectangles:
                start, end = rectangle[si], rectangle[ei]
                if prev_end <= start:
                    count += 1
                prev_end = max(prev_end, end)

            return count + end - prev_end
    
        rectangles.sort(key=lambda x: (x[0], x[2]))
        if checkValid(0, 2) >= 2:
            return True

        rectangles.sort(key=lambda x: (x[1], x[3]))
        return checkValid(1, 3) >= 2
        
