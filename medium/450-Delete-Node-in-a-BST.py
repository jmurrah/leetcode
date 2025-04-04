"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

    Search for a node to remove.
    If the node is found, delete the node.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLargest(self, r):
        if not r.right:
            return r
        
        node = self.getLargest(r.right)
        if node == r.right:
            r.right = node.left
            node.left = None
            
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(r):
            if not r:
                return None
            
            if r.val != key:
                if r.val > key:
                    r.left = dfs(r.left)
                else:
                    r.right = dfs(r.right)
                return r
            
            if not r.left and not r.right:
                return None

            if r.left:
                node = self.getLargest(r.left)
                if node != r.left:
                    node.left = r.left
                node.right = r.right
                r = node
            elif r.right:
                r = r.right
            return r

        return dfs(root)
