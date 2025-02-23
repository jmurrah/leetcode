"""
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of 
distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.post_idxs = {n: i for i, n in enumerate(postorder)}
        self.i = 0

        def dfs(start, end):
            if start > end:
                return None, (1, 0)

            node = TreeNode(preorder[self.i])
            self.i += 1

            left, right_range = dfs(start, self.post_idxs[node.val] - 1)
            right, _ = dfs(right_range[0], right_range[1])

            node.left = left
            node.right = right
            return node, (self.post_idxs[node.val] + 1, end)

        return dfs(0, len(postorder)-1)[0]
