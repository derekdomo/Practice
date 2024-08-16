def remove_duplicate(s):
    cur = None
    dup = False
    stack = []
    for c in s:
        if c != cur:
            if not dup:
                stack.append(cur)
                dup = False
                cur = c
            elif len(stack) > 0 and c == stack[-1]:
                cur = stack.pop()
                dup = True
            else:
                cur = c
                dup = False
        else:
            dup = True
    if not dup:
        stack.append(cur)
    return "".join(stack[1:])

print(remove_duplicate("aabbc"))
print(remove_duplicate("dabbadc"))
print(remove_duplicate("adbbdc"))
print(remove_duplicate(""))
        

