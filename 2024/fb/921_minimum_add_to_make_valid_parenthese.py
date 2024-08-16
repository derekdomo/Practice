class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if len(stack) == 0:
                    count += 1
                else:
                    stack.pop()

        return count + len(stack)
