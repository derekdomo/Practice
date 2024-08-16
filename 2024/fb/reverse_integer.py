class Solution:
    def reverse(self, x):
        if x > 0:
            s = list(str(x))
            s = s[::-1]
            return int("".join(s))
        else:
            s = list(str(-x))
            s = s[::-1]
            return -int("".joint(s))

sol = Solution()
print(sol.reverse(120))
