"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        f, s = dummy, dummy.next

        while s:
            if s.val == val:
                f.next = s.next
            else:
                f = s
            s = s.next
        
        return dummy.next
