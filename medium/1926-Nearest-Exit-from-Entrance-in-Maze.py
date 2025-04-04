"""
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). 
You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. 
Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.
"""


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        entrance = tuple(entrance)
        dq, level = deque([entrance]), -1
        
        seen = set([entrance])
        while dq:
            level += 1
            for _ in range(len(dq)):
                r, c = dq.popleft()
                for ro, co in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    row, col = r + ro, c + co
                    if not (0 <= row < len(maze) and 0 <= col < len(maze[0])):
                        if (r, c) != entrance:
                            return level
                    elif maze[row][col] == "." and (row, col) not in seen:
                        seen.add((row, col))
                        dq.append((row, col))
        
        return -1
        
