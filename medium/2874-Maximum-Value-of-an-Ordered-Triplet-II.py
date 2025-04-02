"""
Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].
"""


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        for i in range(len(nums)-1, -1, -1):
            dp[i] = max(dp[i+1], nums[i])

        output = l = r = 0
        while r < len(nums) - 1:
            while l < r and nums[l] < nums[r]:
                l += 1
            output = max(output, (nums[l] - nums[r]) * dp[r + 1])
            r += 1
        
        return output
