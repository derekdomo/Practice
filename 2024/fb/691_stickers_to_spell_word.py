class Solution:
    def dfs(stickers, target_dict, cache):
        if len(target_dict) == 0:
            return 0
        if len(stickers) == 0:
            return math.inf

        s = ''.join(target_dict.elements())
        key = (len(stickers), s)

        if key in cache:
            return cache[key]

        ret = dfs(stickers[1:], target_dict.copy(), cache)
        from collections import Counter
        counter = Counter(stickers[0])
        
        updated = False
        for k,v in counter.items():
            if k in target_dict:
                target_dict[k] -= v
                if target_dict[k] <= 0:
                    del target_dict[k]
                updated = True

        if updated:
            ret = min(ret, 1 + dfs(stickers, target_dict.copy(), cache))

        cache[key] = ret
        return cache[key]
    

    cache = {}
    from collections import Counter
    counter_char = Counter(target)
    return dfs(stickers, counter_char, cache)


