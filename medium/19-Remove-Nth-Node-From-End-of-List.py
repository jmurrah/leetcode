"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = ListNode(0, head)
        first = second = p

        for i in range(n+1):
            first = first.next

        while first:
            first, second = first.next, second.next
    
        second.next = second.next.next
        return p.next
