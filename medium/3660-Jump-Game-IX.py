"""
You are given an integer array nums.

From any index i, you can jump to another index j under the following rules:

    Jump to index j where j > i is allowed only if nums[j] < nums[i].
    Jump to index j where j < i is allowed only if nums[j] > nums[i].

For each index i, find the maximum value in nums that can be reached by following any sequence of valid jumps starting at i.

Return an array ans where ans[i] is the maximum value reachable starting from index i.
"""


class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [nums[0]] * n
        suf = [nums[-1]] * n

        for i in range(1, len(nums)):
            pre[i] = max(nums[i], pre[i-1])
        
        for i in range(len(nums)-2, -1, -1):
            suf[i] = min(nums[i], suf[i+1])
        
        output = [pre[-1]] * n
        for i in range(len(nums)-2, -1, -1):
            output[i] = pre[i]
            if pre[i] > suf[i + 1]:
                output[i] = output[i + 1]
        
        return output
