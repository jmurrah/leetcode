"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output, q = [], deque()
        l = 0

        for r in range(len(nums)):
            while q and nums[r] > q[-1][0]:
                q.pop()
            q.append((nums[r], r))

            if r + 1 < k: continue

            output.append(q[0][0])
            if q and q[0][1] == l:
                q.popleft()
            l += 1

        return output
