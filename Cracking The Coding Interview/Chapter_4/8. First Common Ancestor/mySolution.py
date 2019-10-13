# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def firstCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.firstCommonAncestor(root.left, p, q)
        right = self.firstCommonAncestor(root.right, p, q)
        if left and right:
            return root
        else:
            return left if left else right
            