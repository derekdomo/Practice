class Solution:
    def isMatch(self, s, p):
        if len(s) == 0:
            if len(p) == 0:
                return True
            elif len(p) == 1:
                return False
            elif len(p) == 2 and p[-1] == '*':
                return True
            else:
                if p[1] == '*':
                    return self.isMatch(s, p[2:])
                else:
                    return False

        elif len(p) == 0:
            return False
        elif s[0] == p[0] or p[0] == '.':
            if len(p) == 1 or p[1] != '*':
                return self.isMatch(s[1:], p[1:])
            else:
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
        else:
            if len(p) == 1 or p[1] != '*':
                return False
            else:
                return self.isMatch(s, p[2:])
