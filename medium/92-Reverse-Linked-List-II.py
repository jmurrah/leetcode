"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, 
and return the reversed list.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head
        
        dummy = cd = ListNode(0, head)
        nodes, add = [], False
        index, current = 1, head

        while current:
            if index == left: 
                add = True

            if add:
                nodes.append(current.val)
            else:
                cd = cd.next

            if index == right:
                for node in nodes[::-1]:
                    cd.next = ListNode(node)
                    cd = cd.next
                cd.next = current.next
                break
    
            index += 1
            current = current.next

        return dummy.next
