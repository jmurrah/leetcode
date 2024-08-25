# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(r, left, right):
            if r:
                return dfs(r.left, left, r.val) and dfs(r.right, r.val, right) if left < r.val < right else False
            return True

        return dfs(root, float("-inf"), float("inf"))
