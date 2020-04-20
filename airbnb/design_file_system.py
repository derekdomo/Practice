'''
You are asked to design a file system which provides two functions:

createPath(path, value): Creates a new path and associates a value to it if possible and returns True. Returns False if the path already exists or its parent path doesn't exist.
get(path): Returns the value associated with a path or returns -1 if the path doesn't exist.
The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

Implement the two functions.

Please refer to the examples for clarifications.

Example 1:

Input:
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
Output:
[null,true,1]
Explanation:
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1
Example 2:

Input:
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
Output:
[null,true,true,2,false,-1]
Explanation:
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/leet", 1); // return true
fileSystem.createPath("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist.
'''
class FileNode:
    def __init__(self, value):
        self.value = value
        self.children = {}

class Solution:
    def __init__(self):
        # tba
        self.root = FileNode(-1)
        self.root.children[""] = FileNode(None)

    def createPath(self, path, value):
        fs = path.split("/")
        cur = self.root
        for i, f in enumerate(fs):
            if f not in cur.children:
                if i != len(fs)-1:
                    return False
                cur.children[f] = FileNode(None)
            cur = cur.children[f]
        cur.value = value

        return True

    def get(self, path):
        fs = path.split("/")
        cur = self.root
        for f in fs:
            if f not in cur.children:
                return -1
            else:
                cur = cur.children[f]

        if cur.value != None:
            return cur.value
        return -1

if __name__ == '__main__':
    sol = Solution()
    print sol.createPath('/leet/code', 2)
    print sol.createPath('/leet', 1)
    print sol.get('/leet')
