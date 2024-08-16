'''
Given a 2-D grid of characters board and a list of strings words, return all 
words that are present in the grid.

For a word to be present it must be possible to form the word with a path in 
the board with horizontally or vertically neighboring cells. The same cell may 
not be used more than once in a word.


'''

class Solution:
    def findWords(self, board, words):
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.isWord = False


        root = TrieNode()
        for word in words:
            cur = root
            for c in word:
                if c in cur.children:
                    cur = cur.children[c]
                else:
                    cur.children[c] = TrieNode()
                    cur = cur.children[c]

            cur.isWord = True

        def dfs(board, i, j, node, visited, cur_word, words):
            if node.isWord:
                words.add(cur_word)
            directions = [(1,0), (0,1), (-1, 0), (0, -1)]
            visited((i, j))
            for direction in directions:
                n_i = i + direction[0]
                n_j = j + direction[1]
                if n_i < 0 or n_j < 0  or n_i>=len(board) or n_j>=len(board[0]):
                    continue 
                if (n_i, n_j) in visited:
                    continue
                if board[n_i][n_j] in node.children:
                    dfs(board, n_i, n_j, node.children[board[n_i][n_j]], visited, cur_word + board[n_i][n_j], words)
            visited.remove((i, j))

        words = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.children:
                    dfs(board, i, j, root.children[board[i][j]], set(), "", words)

        return list(words)


