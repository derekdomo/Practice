'''
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
'''

class Solution:
    def maximumSwap(self, num: int) -> int:
        cur = 1
        digits = list(str(num))
        while cur < len(digits):
            if int(digits[cur]) <= int(digits[cur-1]):
                cur += 1
            else:
                break

        if cur == len(digits):
            return num

        max_n = int(digits[cur])
        ind = cur
        for i in range(cur+1, len(digits)):
            if max_n <= int(digits[i]):
                max_n = int(digits[i])
                ind = i


        for i in range(cur):
            if max_n > int(digits[i]):
                t = digits[i]
                digits[i] = str(max_n)
                digits[ind] = str(t)
                break

        return int(''.join(digits))


sol = Solution()
print(sol.maximumSwap(2736))
print(sol.maximumSwap(9973))
print(sol.maximumSwap(8769))
