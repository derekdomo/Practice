class Solution:
    def chain_words_to_circle(self, arr):
        first_word = arr[0]
        dic = self.form_dict_based_on_first_char(arr[1:])
        num_words = len(arr)-1
        return self.dfs_helper(dic, first_word, first_word, {}, num_words)

    def form_dict_based_on_first_char(self, arr):
        dic = {}
        for word in arr:
            first_char = word[0]
            if first_char in dic:
                dic[first_char].append(word)
            else:
                dic[first_char] = [word]
        return dic

    def dfs_helper(self, dic, first_word, cur_word, visited, num_words):
        if num_words == len(visited.keys()):
            if first_word[0] == cur_word[-1]:
                return True
            else:
                return False
        for word in dic[first_word[-1]]:
            if visited.has_key(word):
                continue
            visited[word] = 1
            if self.dfs_helper(dic, first_word, word, visited, num_words):
                return True
            del visited[word]
        return False 

if __name__ == '__main__':
    sol = Solution()
    print sol.chain_words_to_circle(['abs', 'sss', 'sba'])
