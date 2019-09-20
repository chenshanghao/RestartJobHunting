# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTBranch(root, float('-inf'), float('inf'))
    
    def isValidBSTBranch(self, root, left, right):
        if not root:
            return True
        if not (left < root.val < right):
            return False
            
        return self.isValidBSTBranch(root.left, left, root.val) and self.isValidBSTBranch(root.right, root.val, right)
        
        