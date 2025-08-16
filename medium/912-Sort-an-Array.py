"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
"""


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(l, r):
            if r <= l:
                return

            p = (l + r) // 2
            ls, rs = l, r
            nums[p], nums[r] = nums[r], nums[p]

            r -= 1
            while l <= r:
                while l <= r and nums[l] < nums[rs]:
                    l += 1
                while l <= r and nums[r] > nums[rs]:
                    r -= 1
                if l <= r:
                     nums[l], nums[r] = nums[r], nums[l]
                     l += 1
                     r -= 1

            nums[l], nums[rs] = nums[rs], nums[l]
            quicksort(ls, l-1)
            quicksort(l+1, rs)
        
        quicksort(0, len(nums)-1)
        return nums
