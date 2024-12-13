"""
You are given an array nums consisting of positive integers.

Starting with score = 0, apply the following algorithm:

    Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
    Add the value of the chosen integer to score.
    Mark the chosen element and its two adjacent elements if they exist.
    Repeat until all the array elements are marked.

Return the score you get after applying the above algorithm.
"""


class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = set()
        h = [(num, i) for i, num in enumerate(nums)]
        score = 0

        heapq.heapify(h)

        while h:
            num, index = heapq.heappop(h)
            if index in marked:
                continue
                
            marked.add(index)
            if index != 0: marked.add(index-1)
            if index != len(nums)-1: marked.add(index+1)
            score += nums[index]
        
        return score
