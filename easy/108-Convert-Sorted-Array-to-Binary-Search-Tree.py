"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        m = (len(nums)-1) // 2
        r = TreeNode(nums[m])

        r.left = self.sortedArrayToBST(nums[:m])
        r.right = self.sortedArrayToBST(nums[m+1:])
        
        return r