"""
Given the head of a linked list, return the list after sorting it in ascending order.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def merge(self, left: [ListNode], right: [ListNode]) -> [ListNode]:
        lc, rc = left, right
        dummy = curr = ListNode()

        while lc or rc:
            if not rc or (rc and lc and lc.val <= rc.val):
                curr.next = lc
                lc = lc.next
            else:
                curr.next = rc
                rc = rc.next
            curr = curr.next
        
        return dummy.next


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        
        last_half = s.next
        s.next = None

        return self.merge(self.sortList(head), self.sortList(last_half))
