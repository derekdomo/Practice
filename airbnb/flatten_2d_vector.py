'''
Example 1:

Input:[[1,2],[3],[4,5,6]]
Output:[1,2,3,4,5,6]
Example 2:

Input:[[7,9],[5]]
Output:[7,9,5]
'''


class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.vec2d = vec2d
        self.cur_ind = [(0,0)]


    # @return {int} a next element
    def next(self):
        # Write your code here
        self.hasNext()
        i, j = self.cur_ind.pop()
        ret = self.vec2d[i][j]
        self.cur_ind.append((i, j+1))
        return ret


    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        if len(self.cur_ind) == 0:
            return False
        i, j = self.cur_ind.pop()
        if i >= len(self.vec2d):
            return False
        elif j >= len(self.vec2d[i]):
            i += 1
            j = 0
            self.cur_ind.append((i, j))
            return self.hasNext()
        else:
            self.cur_ind.append((i, j))
            return True

if __name__ == '__main__':
    vec2d = Vector2D([[7,9],[5]])
    while vec2d.hasNext():
        print vec2d.next()

