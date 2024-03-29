# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isSymmetricPair(root.left, root.right)
        
    def isSymmetricPair(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        else:
            return self.isSymmetricPair(left.left, right.right) and self.isSymmetricPair(right.left, left.right) 
        
        
        