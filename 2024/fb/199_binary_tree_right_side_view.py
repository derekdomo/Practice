from typing import List
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        from collections import deque
        queue = deque([root, None])
        pre = None
        ret = []
        while len(queue) > 0:
            node = queue.popleft()
            if node == None:
                ret.append(pre.val)
                if len(queue) == 0:
                    return ret
                queue.append(None)
                pre = None
                continue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            pre = node
