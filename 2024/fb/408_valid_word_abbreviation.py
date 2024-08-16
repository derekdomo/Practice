class Solution:
    def validWordAbbreviation(self, word: str, abbr: str):
        cur_word = 0
        cur_abb = 0
        while cur_word < len(word) or cur_abb < len(abbr):
            if cur_word == len(word) or cur_abb == len(abbr):
                return False

            if not abbr[cur_abb].isnumeric():
                if abbr[cur_abb] != word[cur_word]:
                    return False
                cur_abb += 1
                cur_word += 1
            else:
                n = 0
                while cur_abb < len(abbr) and abbr[cur_abb].isnumeric():
                    n = int(abbr[cur_abb]) + n * 10
                    cur_abb += 1

                cur_word += n 
                if cur_word > len(word):
                    return False

        return True

sol = Solution()
print(sol.validWordAbbreviation('internationalization', 'i12iz4n'))
print(sol.validWordAbbreviation('apple', 'a2e'))
