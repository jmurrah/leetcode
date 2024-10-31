"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the 
problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode(0, head)
        curr = head

        while curr and curr.next:
            temp = curr.next.next
            prev.next, prev.next.next = curr.next, curr
            curr.next = temp
            curr, prev = curr.next, prev.next.next
        
        return dummy.next
