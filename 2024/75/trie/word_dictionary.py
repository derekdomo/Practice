class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                cur.children[c] = TrieNode
                cur = cur.children[c]

        cur.isWord = True


    def search(self, word):
        def dfs(node, word):
            if len(word) == 0:
                return node.isWord
            if word[0] == '.':
                for k in node.children:
                    if dfs(node.children[k], word[1:]):
                        return True
            else:
                if word[0] in node.children:
                    return dfs(node.children[n], word[1:])
                else:
                    return False

        return search(self.root, word)

