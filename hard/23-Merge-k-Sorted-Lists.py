"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        current_nodes, i = [], 0
        for head in lists:
            if head: 
                heappush(current_nodes, (head.val, i, head))
                i += 1

        output = curr = ListNode(-1, None)
        while current_nodes:
            _, i, node = heappop(current_nodes)
            curr.next = node
            curr = curr.next
            if node.next:
                heappush(current_nodes, (node.next.val, i, node.next))
        
        return output.next
