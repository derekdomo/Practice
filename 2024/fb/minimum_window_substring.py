def minimum_window_substring(s, t):
    from collections import Counter
    counter = Counter(t)
    left = 0
    right = 0
    required = len(counter)
    res = None
    import math
    min_len = math.inf
    # left is exclusive but right is inclusive
    while right < len(s):
        c = s[right]
        if c in counter:
            counter[c] -= 1
            if counter[c] == 0:
                required -= 1

        while left<=right and required == 0:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                res = s[left:right+1]
            c = s[left]
            if c in counter:
                counter[c] += 1
                if counter[c] > 0:
                    required += 1
            left += 1
        right += 1
    return res, min_len

print(minimum_window_substring("ADOBECODEBANC", "ABC"))
print(minimum_window_substring("ADOBECODEBANC", "ABC"))

