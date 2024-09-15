"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        heapify(h)

        for n in nums:
            heappush(h, -n)

        while k > 1:
            k -= 1
            heappop(h)
        
        return -h[0]
