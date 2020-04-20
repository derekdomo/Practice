'''
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
Example 1:
Given the following words in dictionary,
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf".
Example 2:
Given the following words in dictionary,
[
  "z",
  "x"
]
The correct order is: "zx".
'''

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        # build directional graph
        graph = {}
        degrees = {}
        for i in xrange(1, len(words)):
            wordA = words[i-1]
            wordB = words[i]
            prev, later = self._findDifferentChar(wordA, wordB)
            if prev == None:
                continue
            graph[prev] = graph.get(prev, set()) | {later}
            degrees[prev] = degrees.get(prev, 0)
            degrees[later] = degrees.get(later, 0) + 1
        order = []
        from collections import deque
        queue = deque()
        for k in degrees.keys():
            if degrees[k] == 0:
                queue.append(k)
                del degrees[k]

        while len(queue) > 0:
            zero_c = queue.popleft() 
            order.append(zero_c)
            for neighbor in graph.get(zero_c, set()):
                degrees[neighbor] -= 1
                if degrees[neighbor] == 0:
                    queue.append(neighbor)
                    del degrees[neighbor]


        if len(degrees) != 0:
            return []
        return order


    def _findDifferentChar(self, wordA, wordB):
        for i in xrange(len(wordA)):
            if wordA[i] != wordB[i]:
                return wordA[i], wordB[i]
        return None, None

if __name__ == '__main__':
    sol = Solution()
    #print sol.alienOrder(["wrt","wrf","er","ett","rftt"])
    print sol.alienOrder(["z", "x", "z"])
    print sol.alienOrder(["wrt","wrf","er","ett","rftt","te"])
    print sol.alienOrder(["wrt","wrf","er","ett","rftt"])
