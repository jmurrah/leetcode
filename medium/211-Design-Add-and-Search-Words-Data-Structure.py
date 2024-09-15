"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. 
word may contain dots '.' where dots can be matched with any letter.

"""


class TrieNode:
    def __init__(self, children, end):
        self.children = children
        self.end = end

class WordDictionary:

    def __init__(self):
        self.root = TrieNode({}, False)

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode({}, False)
            curr = curr.children[c]
        curr.end = True
        
    def search(self, word: str) -> bool:
        def dfs(curr, index):
            for i in range(index, len(word)):
                if word[i] == ".":
                    for char in curr.children:
                        if dfs(curr.children[char], i+1):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]

            return curr.end
        
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
