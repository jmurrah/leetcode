"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(r, current_max):
            if r:
                current_max = max(current_max, r.val)
                add = 1 if r.val == current_max else 0
                return add + dfs(r.left, current_max) + dfs(r.right, current_max)
            return 0

        return dfs(root, root.val)
