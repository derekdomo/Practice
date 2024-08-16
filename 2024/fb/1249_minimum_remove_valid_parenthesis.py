class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # if in the end, cannot close all the parenthesis, remove the opening ones
        # if in the process, meet a closing without an open in the stack, remove it directly
        stack = []
        ret = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append((c, i))
                ret.append(c)
            elif c == ')':
                if len(stack) > 0:
                    stack.pop()
                    ret.append(c)
                else:
                    ret.append('')
            else:
                ret.append(c)

        for to_r, ind in stack:
            ret[ind] = ''

        return ''.join(ret)

sol = Solution()
print(sol.minRemoveToMakeValid("lee(t(c)o)de)"))
