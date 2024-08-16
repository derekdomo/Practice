class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def dfs(root, target, closest):
            if root == None:
                return
            delta = root.val - target
            if abs(delta) == abs(closest[0] - target):
                closest[0] = min(closest[0], root.val)
            elif abs(delta) < abs(closest[0] - target):
                closest[0] = root.val
            
            if root.val == target:
                return
            elif root.val > target:
                dfs(root.left, target, closest)
            else:
                dfs(root.right, target, closest)
        closest = [root.val]
        dfs(root, target, closest)
        return closest[0]
