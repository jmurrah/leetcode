"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
"""


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return nums

        def merge(l1, l2):
            combined = []
            while l1 and l2:
                if l1[0] < l2[0]:
                    combined.append(l1[0])
                    l1.popleft()
                else:
                    combined.append(l2[0])
                    l2.popleft()
            
            while l1 or l2:
                if l1:
                    combined.append(l1[0])
                    l1.popleft()
                else:
                    combined.append(l2[0])
                    l2.popleft()
            
            return combined

        m = len(nums) // 2
        l1 = deque(self.sortArray(nums[:m]))
        l2 = deque(self.sortArray(nums[m:]))
        return merge(l1, l2)
