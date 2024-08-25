"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        s = [float("-inf")]
        
        def dfs(r):
            if r:
                left = dfs(r.left)
                right = dfs(r.right)
                s[0] = max(s[0], r.val, r.val + left + right, r.val + left, r.val + right)
                return max(r.val, r.val + left, r.val + right)
            return 0

        dfs(root)
        return s[0]
