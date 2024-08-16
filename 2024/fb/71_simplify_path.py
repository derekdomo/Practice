class Solution:
    def simplifyPath(self, path):
        stack = ['']
        folders = path.split('/')
        for folder in folders:
            if folder == '' or folder == '.':
                continue
            elif folder == '..':
                if len(stack) > 1:
                    stack.pop()
            else:
                stack.append(folder)

        if len(stack) == 1:
            return '/'
        return '/'.join(stack)
