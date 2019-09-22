# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.inorderTravel(root, res)
        return res
    
    def inorderTravel(self, node, res):
        if not node:
            return
        if node.left:
            self.inorderTravel(node.left, res)
        res.append(node.val)
        if node.right:
            self.inorderTravel(node.right, res)
