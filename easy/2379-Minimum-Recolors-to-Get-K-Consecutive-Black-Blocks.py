"""
You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. 
The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.
"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        d = {"W": 0, "B": 0}
        for block in blocks[:k]:
            d[block] += 1

        output = d["W"]
        for r in range(k, len(blocks)):
            d[blocks[r-k]] -= 1
            d[blocks[r]] += 1
            output = min(output, d["W"])
        
        return output
