"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow = slow.next
        
        prev = None
        while slow:
            prev, prev.next, slow = slow, prev, slow.next
        
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        
        return True
