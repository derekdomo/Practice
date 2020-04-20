class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(-1)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        cur = self.root
        for c in word:
            if c not in cur.children: 
                cur.children[c] = TrieNode(c)
            cur = cur.children[c]

        cur.word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._dfs(word, self.root)
    
    def _dfs(self, word, node):
        if len(word) == 0:
            return node.word
        c = word[0]
        if c == '.':
            for n_c in node.children:
                if self._dfs(word[1:], node.children[n_c]):
                    return True
            return False
        else:
            if c not in node.children:
                return False
            return self._dfs(word[1:], node.children[c])

class TrieNode:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.word = False

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("......")
print obj.search('abc')

