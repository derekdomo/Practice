'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
'''
class Solution:
    def pow(self, x, n):
        cache = {}
        def dfs(x, n, cache):
            if n == 1:
                cache[n] = x
                return x
            left = n // 2
            right = n - left
            cache[n] = dfs(x, left, cache) * dfs(x, right, cache)

            return cache[n]

        if n < 0:
            return pow(x, -n)
        else:
            return dfs(x, n, cache)

sol = Solution()
print(sol.pow(2.000, 10))
