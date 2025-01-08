"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites 
where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. 
If it is impossible to finish all courses, return an empty array.
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for cla, pre in prerequisites:
            adj[cla].append(pre)
        
        course_order = []
        seen = set()

        def dfs(node, curr_path):
            if node in curr_path:
                return False
            if node in seen:
                return True

            seen.add(node)
            curr_path.add(node)
            for n in adj[node]:
                if not dfs(n, curr_path):
                    return False

            curr_path.remove(node)
            course_order.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i, set()):
                return []
        
        return course_order
