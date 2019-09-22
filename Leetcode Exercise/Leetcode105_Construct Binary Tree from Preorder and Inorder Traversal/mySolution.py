# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = ListNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: index + 1], inorder[0: index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root