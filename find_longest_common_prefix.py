class Trie(object):
    def __init__(self):
        self.word_count = 0
        self.map = {}

def construct_word(words):
    root = Trie()
    for word in words:
        cur = root
        cur.word_count += 1
        for c in word:
            if c in cur.map:
                cur = cur.map[c]
            else:
                cur.map[c] = Trie()
                cur = cur.map[c]
            cur.word_count += 1
    res = [""]
    dfs(root, res, "")
    return res[0]
    

def dfs(root, res, cur_res):
    if root.word_count == 1:
        if len(cur_res)-1 > len(res[0]):
            res[0] = cur_res[:-1]
        return

    for c in root.map:
        dfs(root.map[c], res, cur_res+c)


print construct_word(['aaaa', 'aaab', 'ssss', 'eeeee', 'aab'])

