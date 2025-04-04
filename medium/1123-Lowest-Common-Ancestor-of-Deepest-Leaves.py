"""
Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

    The node of a binary tree is a leaf if and only if it has no children
    The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
    The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(r, depth):
            if not r:
                return None, float("-inf")

            left, left_depth = dfs(r.left, depth + 1)
            right, right_depth = dfs(r.right, depth + 1)

            if left_depth == right_depth:
                return r, max(depth, left_depth)
            if left_depth > right_depth:
                return left, left_depth
            return right, right_depth

        return dfs(root, 0)[0]
