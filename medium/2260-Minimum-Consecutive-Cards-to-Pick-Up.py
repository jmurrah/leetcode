"""
You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. 
If it is impossible to have matching cards, return -1.
"""


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        locations = {}
        min_consecutive = float("inf")

        for r, value in enumerate(cards):
            if value in locations:
                min_consecutive = min(r - locations[value] + 1, min_consecutive)
            
            locations[value] = r
        
        return min_consecutive if min_consecutive != float("inf") else -1
