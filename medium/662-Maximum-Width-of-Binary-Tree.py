"""
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes 
that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dq = deque([(root, 1)])
        max_width = 0

        while dq:
            max_width = max(max_width, dq[0][1] - dq[-1][1] + 1)
            for _ in range(len(dq)):
                node, val = dq.pop()
                if node.left:
                    dq.appendleft((node.left, val * 2))
                if node.right:
                    dq.appendleft((node.right, (val * 2) + 1))

        return max_width
