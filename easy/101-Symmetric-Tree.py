"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(r1, r2):
            if r1 and r2:
                if r1.val != r2.val:
                    return False
                return dfs(r1.left, r2.right) and dfs(r1.right, r2.left)
            return not r1 and not r2
        
        return dfs(root.left, root.right)
