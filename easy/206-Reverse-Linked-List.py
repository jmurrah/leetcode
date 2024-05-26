"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c, r = head, None

        while c:
            placeholder = ListNode(c.val)
            placeholder.next = r if r else None
            r = placeholder
            c = c.next
        
        return r
