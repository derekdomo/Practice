'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

'''

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        def build_masked_map(words):
            from collections import defaultdict
            masked_map = defaultdict(list)
            inverted_map = defaultdict(list)
            for word in words:
                for i in range(len(word)):
                    masked_word = word[:i] + '*' + word[i+1:]
                    masked_map[masked_word].append(word)
                    inverted_map[word].append(masked_word)
            return masked_map, inverted_map
        masked_word_map, inverted_map = build_masked_map(wordList + [startWord])
        from collections import deque
        queue = dequeue([(beginWord, 0)])
        visited = set()
        while len(queue) > 0:
            word, step = queue.popleft()
            if word in visited:
                continue
            if word == endWord:
                return step
            visited.add(word)
            for masked_word in inverted_map[word]:
                for new_word in masked_word_map[masked_word]:
                    if new_word in visited:
                        continue
                    queue.append((new_word, step+1))
        return 0
        


