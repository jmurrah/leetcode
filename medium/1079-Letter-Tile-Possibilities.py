"""
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.
"""


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count_tiles = Counter(tiles)
        self.count = 0
        
        def backtrack():
            for tile in count_tiles:
                if count_tiles[tile] == 0:
                    continue
                self.count += 1

                count_tiles[tile] -= 1
                backtrack()
                count_tiles[tile] += 1
        
        backtrack()
        return self.count
