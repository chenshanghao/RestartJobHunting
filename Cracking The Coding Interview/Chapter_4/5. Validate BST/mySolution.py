# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.checkValidBST(root, float('-inf'), float('inf'))
    
    def checkValidBST(self, node, left, right):
        if not node:
            return True
        if not (left < node.val < right):
            return False
        return self.checkValidBST(node.left, left, node.val) and self.checkValidBST(node.right, node.val, right)