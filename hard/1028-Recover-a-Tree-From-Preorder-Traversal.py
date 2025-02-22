"""
We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  
If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack, i, lt = [], 0, len(traversal)

        while i < lt:
            j = i
            while j < lt and not traversal[j].isdigit():
                j += 1
            level = j - i

            i = j
            while j < lt and traversal[j].isdigit():
                j += 1
            node = TreeNode(int(traversal[i:j]))

            while len(stack) > level:
                stack.pop()

            if stack and not stack[-1].left:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
                
            stack.append(node)
            i = j

        while len(stack) > 1:
            stack.pop()

        return stack[0]
