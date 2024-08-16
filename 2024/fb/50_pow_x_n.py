class Solution:
    def myPow(self, x, n):
        def dfs(x, n, cache):
            if n == 0:
                return 1
            if n == 1:
                return x
            if (x, n) in cache:
                return cache[x, n]
            left = n // 2
            right = n - left
            ret = dfs(x, right, cache) * dfs(x, left, cache)
            cache[(x, n-1)] = ret
            return ret

        if n < 0:
            return 1/dfs(x, -n, {})
        else:
            return dfs(x, n, {})

