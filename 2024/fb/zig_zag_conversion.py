class Solution:
    def convert(self, s, numRows):
        arr = ["" for i in range(numRows)]
        zigzag = False
        cur = 0
        for c in s:
            if not zigzag:
                arr[cur] += c
                cur += 1
            else:
                arr[cur] += c
                cur -= 1
            if cur == numRows-1:
                zigzag = True
            elif cur == 0:
                zigzag = False
        return "".join(arr)

sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))
print(sol.convert("PAYPALISHIRING", 4))


                
