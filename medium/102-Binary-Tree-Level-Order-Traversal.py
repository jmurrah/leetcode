"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue, output = deque(), []
        queue.append(root)

        while queue:
            length, lvl = len(queue), []
            for i in range(length):
                node = queue.popleft()
                if node:
                    lvl.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if lvl: output.append(lvl)
        
        return output
