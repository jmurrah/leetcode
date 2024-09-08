"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites 
where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {i: set() for i in range(numCourses)}
        visited = set()

        def dfs(current):
            if current in visited:
                return False
            if not d[current]:
                return True

            visited.add(current)
            for p in d[current]:
                if not dfs(p):
                    return False
                    
            d[current] = set()
            visited.remove(current)
            return True

        for cla, pre in prerequisites:
            d[cla].add(pre)
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
