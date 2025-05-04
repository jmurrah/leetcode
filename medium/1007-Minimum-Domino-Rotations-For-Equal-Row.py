"""
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.
"""


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        counts = defaultdict(int)
        m = (-1, -1)

        for i in range(len(tops)):
            counts[tops[i]] += 1
            counts[bottoms[i]] += 1
            if counts[tops[i]] > m[0]:
                m = (counts[tops[i]], tops[i])
            if counts[bottoms[i]] > m[0]:
                m = (counts[bottoms[i]], bottoms[i])
        
        val = m[1]
        if not all([tops[i] == val or bottoms[i] == val for i in range(len(tops))]):
            return -1
        
        mt = mb = 0
        for i in range(len(tops)):
            mt += int(tops[i] != val)
            mb += int(bottoms[i] != val)

        return min(mt, mb)
