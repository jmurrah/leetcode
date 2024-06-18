"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        out = set()
        
        def dfs(root, h):
            if root and not root.left and not root.right:
                out.add(h)
            elif not root:
                return
            else:
                dfs(root.left, h + 1)
                dfs(root.right, h + 1)

        dfs(root, 1)
        return min(out) if out else 0
