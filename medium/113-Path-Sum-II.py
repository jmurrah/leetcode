"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []

        def dfs(r, curr, total):
            if not r:
                return False
            
            curr.append(r.val)
            total += r.val
            
            left = dfs(r.left, curr, total)
            right = dfs(r.right, curr, total)
            
            if not left and not right and total == targetSum:
                paths.append(curr.copy())

            curr.pop()
            return True
        
        dfs(root, [], 0)
        return paths
