'''
Given the root of a non-empty binary tree, return the maximum path sum of any 
non-empty path.

A path in a binary tree is a sequence of nodes where each pair of adjacent 
nodes has an edge connecting them. A node can not appear in the sequence more 
than once. The path does not necessarily need to include the root.

The path sum of a path is the sum of the node's values in the path.

Example 1:

Input: root = [1,2,3]

Output: 6
Explanation: The path is 2 -> 1 -> 3 with a sum of 2 + 1 + 3 = 6.

Example 2:

Input: root = [-15,10,20,null,null,15,5,-5]

Output: 40
Explanation: The path is 15 -> 20 -> 5 with a sum of 15 + 20 + 5 = 40.
'''
class Solution:
    def maxPathSum(self, root):
        # left maximum sum, right maximum sum, root,

        max_sum = [root.val]
        if root == None:
            return max_sum

        def calculateSum(root, max_sum):
            if root == None:
                return 0
            if root.left == None and root.right == None:
                return root.val
            
            left_side = calculateSum(root.left)
            right_side = calculateSum(root.right)
            max_sum[0] = max(max_sum[0], left_side, right_side, 
                          left_side+root.val+right_side,
                          left_side+root.val, root.val+right_side)
            return max(left_side+root.val, right_side+root.val, root.val)

        calculateSum(root, max_sum)
        return max_sum[0]
