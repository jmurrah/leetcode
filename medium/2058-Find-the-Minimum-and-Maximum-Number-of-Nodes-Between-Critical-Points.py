"""
A critical point in a linked list is defined as either a local maxima or a local minima.

A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the 
minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct 
critical points. If there are fewer than two critical points, return [-1, -1].
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        pos, index, min_diff = [], 1, float("inf")
        prev, current = head, head.next

        while current.next:
            if (current.val > prev.val and current.val > current.next.val) or (
                current.val < prev.val and current.val < current.next.val
            ):
                if pos: min_diff = min(min_diff, index - pos[-1])
                pos.append(index)

            prev = prev.next
            current = current.next
            index += 1

        if len(pos) < 2:
            return [-1, -1]

        max_diff = pos[-1] - pos[0]
        return [min_diff, max_diff]
