class Solution:
    def isNumber(s):
        if s == '' or s is None:
            return False
        left = 0
        right = len(s) - 1
        while left <= right and (s[left] == ' ' or s[right] == ' '):
            if s[left] == ' ':
                left += 1
            if s[right] == ' ':
                right -= 1

        if left > right:
            return False

        if s[left] == '+' or s[left] == '-':
            left += 1

        s = s[left:right+1]

        dot_ind = -1
        e_ind = -1
        cur = 0
        while cur < len(s):
            c = s[cur]
            if dot_ind == -1 and c == '.':
                dot_ind = cur
            elif e_ind == -1 and c == 'e':
                e_ind = cur
                if cur < len(s)-1 and s[cur+1] == '+' or s[cur+1] == '-':
                    cur += 1
            elif c.isnumeric():
                cur += 1
            else:
                return False

        # valid case 1: pure numbers
        if dot_ind == -1 and e_ind == -1:
            return True
        elif dot_ind != -1 and e_dot == -1:
            left_n = s[:dot_ind]
            right_n = s[dot_ind+1:]

            if len(left_n) == 0 and len(right_n) == 0:
                return False
            return True
        elif e_ind != -1 and dot_ind == -1:
            if e_ind == len(s) - 1 or e_ind == 0:
                return False
            if s[e_ind+1] == '+' or s[e_ind+1] == '-':
                if e_ind == len(s) - 2:
                    return False
            return True
        else:
            if e_ind < dot_ind:
                return False
            first = s[:dot_ind]
            second = s[dot_ind+1: e_ind]
            if len(first) == 0 and len(second) == 0:
                return False
            if e_dot == len(s) - 1:
                return False
            third = None
            if s[e_ind+1] == '+' or s[e_ind+1] == '-':
                third = s[e_ind+2:]
            else:
                third = s[e_ind+1:]

            if len(th)  == 0:
                return False
            return True






