"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.
"""


class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False

    def add_word(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        output, seen = set(), set()
        trie = TrieNode()

        for word in words:
            trie.add_word(word)

        def dfs(x, y, node, curr):
            if not (0 <= x < len(board) and 0 <= y < len(board[0])) or (x, y) in seen or board[x][y] not in node.children:
                return

            seen.add((x, y))
            curr.append(board[x][y])
            node = node.children[board[x][y]]
            if node.end:
                node.end = False
                output.add("".join(curr))

            dfs(x+1, y, node, curr.copy())
            dfs(x-1, y, node, curr.copy())
            dfs(x, y+1, node, curr.copy())
            dfs(x, y-1, node, curr.copy())
            seen.remove((x, y))

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie, [])
        
        return output
