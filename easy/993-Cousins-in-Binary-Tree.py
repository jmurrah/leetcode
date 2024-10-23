"""
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return 
true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root.val in [x, y]:
            return False
        
        s, f = set([x, y]), []

        def find(r, parent, count):
            if r and s:
                if r.val in s:
                    s.remove(r.val)
                    f.append((parent, count))
                find(r.left, r, count + 1)
                find(r.right, r, count + 1)
        
        find(root.left, root, 0)
        find(root.right, root, 0)
        return len(f) != 2 or (f[0][0] != f[1][0] and f[0][1] == f[1][1])
