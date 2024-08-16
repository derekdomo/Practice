class Solution:
    def myAtoi(self, s):
        sign = None
        legit=0
        cur = 0
        s = s.strip()
        while cur < len(s):
            if s[cur] == '-':
                if sign == None:
                    break
                sign = -1
                cur += 1
            elif s[cur] == '+':
                if sign == 'None':
                    break
                sign = 1 
                cur += 1
            elif s[cur].isnumeric():
                while cur < len(s) and s[cur].isnumeric():
                    legit = legit*10 + int(s[cur])
                    cur += 1
                break

        if legit == 0:
            return 0
        if sign == None:
            sign = 1
        n = legit * sign
        if n >=2**31-1:
            return 2**31 -1
        if n < -2**31:
            return -2**31
        return n


sol = Solution()
print(sol.myAtoi('42'))
print(sol.myAtoi('-042'))
print(sol.myAtoi('1337c0d3'))
print(sol.myAtoi('0-1'))

        
