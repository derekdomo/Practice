def find_ladder(words, begin_word, end_word):
    if begin_word not in words:
        words.append(begin_word)

    from collections import defaultdict
    word_to_mask = defaultdict(list)
    mask_to_word = defaultdict(list)
    for word in words:
        for i, n in enumerate(word):
            mask = word[:i] + "*" + word[i+1:]
            word_to_mask[word].append(mask)
            mask_to_word[mask].append(word)
    
    def dfs(word, visited):
        if word == end_word:
            return True
        if word in visited:
            return False
        visited.add(word)
        for mask in word_to_mask[word]:
            for sim_word in mask_to_word[mask]:
                if sim_word not in visited and dfs(sim_word, visited):
                    return True
        return False

    return dfs(word, set())

words = ["hot","dot","dog","lot","log","cog"]
begin_word = "hit"
end_word = "cog"

print(find_ladder(words, begin_word, end_word))


