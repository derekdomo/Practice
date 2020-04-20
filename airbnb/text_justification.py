'''
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
'''
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        cur_len = 0
        cur_word = 0
        while cur_word < len(words):
            w_l = len(words[cur_word])
            if w_l + cur_len > maxWidth:
                break
            cur_len += w_l + 1
            cur_word += 1

        if cur_word == len(words):
            return [self.constructSentence(words, maxWidth, True)] 
        
        sentence = self.constructSentence(words[:cur_word], maxWidth)

        return [sentence] + self.fullJustify(words[cur_word:], maxWidth)


    def constructSentence(self, words, maxWidth, lastLine=False):
        total_length = 0
        for w in words:
            total_length += len(w)
        
        if len(words) == 1 or lastLine:
            return " ".join(words) + " "*(maxWidth - total_length - len(words) + 1)


        total_blanks = maxWidth - total_length
        blanks = [total_blanks/(len(words)-1)]*(len(words)-1)
        remain_blanks = total_blanks % (len(words)-1)

        for i in xrange(remain_blanks):
            blanks[i] += 1

        sentence = words[0]
        for i, w in enumerate(words[1:]):
            sentence += " "*blanks[i] + w 

        return sentence

if __name__ == '__main__':
    sol = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    print sol.fullJustify(words, maxWidth)
        
            

