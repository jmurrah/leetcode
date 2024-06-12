"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted. 
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q, averages = [root], []

        while q:
            total, lenq = 0, len(q)
            for i in range(lenq):
                node = q.pop(0)
                total += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            averages.append(total / lenq)
        
        return averages
