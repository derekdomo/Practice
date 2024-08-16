class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2 = p, q
        # there might be multiple loops to hit the root
        # p1 and p2 keeps going up until they hit the root
        # if they hit the root, they go back as another node and restart
        # so if we consider the number of steps we go
        # steps_p1 + steps_p2 = steps_p2 + steps_p1
        # steps_p1 + p1_common + common_root = steps_p2 + p2_common + common_root
        while p1 != p2:
            if p1.parent != None:
                p1 = p1.parent
            else:
                p1 = q
            if p2.parent != None:
                p2 = p2.parent
            else:
                p2 = p
        return p1
