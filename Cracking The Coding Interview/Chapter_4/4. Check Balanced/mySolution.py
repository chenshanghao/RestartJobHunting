# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.checkBalanced(root) != -1
    
    def checkBalanced(self, node):
        if not node:
            return 0
        left_depth = self.checkBalanced(node.left) + 1
        right_depth = self.checkBalanced(node.right) + 1
        if left_depth == 0 or right_depth == 0 or abs(right_depth - left_depth) > 1:
            return -1
        else:
            return max(left_depth, right_depth)
        
        
        
        