class Solution:
    def minimum_edit_distance(self, word1, word2):
        # inserting distance
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        # find common character and divide
        minimum_distance = 1000000
        for i in xrange(len(word1)):
            c = word1[i]
            for j in xrange(len(word2)):
                if c == word2[j]:
                   left_distance = self.minimum_edit_distance(word1[0:i], word2[0:j])
                   right_distance = self.minimum_edit_distance(word1[i+1:], word2[j+1:])
                   minimum_distance = min(minimum_distance, left_distance+right_distance)
        # No equal character at all
        minimum_distance = min(max(len(word1), len(word2)), minimum_distance)
        return minimum_distance

if __name__ == '__main__':
    sol = Solution()
    print "abc, ab"
    print sol.minimum_edit_distance("abc", "ab")
    print "cat, dog"
    print sol.minimum_edit_distance("cat", "dog")
    print "cat, cats"
    print sol.minimum_edit_distance("cat", "cats")
    print "cat, cut"
    print sol.minimum_edit_distance("cat", "cut")
    print "cats, casts"
    print sol.minimum_edit_distance("cats", "casts")

