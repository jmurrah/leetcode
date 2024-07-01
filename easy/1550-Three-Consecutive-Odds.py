"""
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false. 
"""


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consecutive = 0

        for num in arr:
            consecutive = consecutive + 1 if num % 2 == 1 else 0
            if consecutive == 3: return True
        
        return False
