"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        def backtrack(current_list):
            if len(current_list) == len(nums):
                output.append(current_list.copy())
                return 

            for number in set(nums) - set(current_list):
                current_list.append(number)
                backtrack(current_list)
                current_list.pop()
        
        backtrack([])
        return output
