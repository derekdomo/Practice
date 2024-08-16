class TrieNode:
    def __init__():
        self.char = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode


    def insert(self, word):
        cur = self.root
        for c in word:
            if c in cur.char:
                cur = cur.char[c]
            else:
                cur.char[c] = TrieNode
                cur = c.char[c]

        cur.isWord = True

    def search(self, word):
        cur = self.root
        for c in word:
            if c in cur.char:
                cur = cur.char[c]
            else:
                return False

        return cur.isWord

    def startsWith(self, prefix):
        cur = self.root
        for c in prefix:
            if c in cur.char:
                cur = cur.char[c]
            else:
                return False

        return True
