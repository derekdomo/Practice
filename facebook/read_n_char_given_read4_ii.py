'''
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:

The read function may be called multiple times.
'''
class Solution(Object):
    def __init__(self):
        self.remain = []

    def read(self, res, n):
        ret = []
        if len(self.remain) != 0:
            res += self.remain
            n = n - len(self.remain)
            self.remain = []

        while n - 4 > 0:
            ret += self.read4()
            n = n-4

        if n == 0:
            return ret
        tmp = self.read4()
        for i in xrange(n):
            ret.append(tmp[i])
        self.remain = tmp[n:]

        return ret
