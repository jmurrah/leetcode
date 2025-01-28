"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites 
where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

    For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.

Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then 
course a is a prerequisite of course c.

You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a 
prerequisite of course vj or not.

Return a boolean array answer, where answer[j] is the answer to the jth query.
"""


class Node:
    def __init__(self, val: int=0, children: list=None):
        self.val = val
        self.children = children if children else []

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if not prerequisites:
            return [False for _ in queries]

        in_degrees = [0] * numCourses
        nodes = {}

        for pre, cla in prerequisites:
            in_degrees[cla] += 1
            if pre not in nodes:
                nodes[pre] = Node(val=pre)
            if cla not in nodes:
                nodes[cla] = Node(val=cla)

            nodes[pre].children.append(nodes[cla])

        prereqs = defaultdict(set)
        dq = deque([node for node in nodes.values() if in_degrees[node.val] == 0])

        while dq:
            node = dq.pop()

            for child in node.children:
                in_degrees[child.val] -= 1

                prereqs[child.val].add(node.val)
                prereqs[child.val].update(prereqs[node.val])

                if in_degrees[child.val] == 0:
                    dq.appendleft(child)

        
        return [u in prereqs[v] for u, v in queries]
