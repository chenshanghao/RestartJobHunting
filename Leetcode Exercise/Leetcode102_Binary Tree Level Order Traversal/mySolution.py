# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            newStack = []
            levelVal = []
            for node in stack:
                levelVal.append(node.val)
                if node.left:
                    newStack.append(node.left)
                if node.right:
                    newStack.append(node.right)
            res.append(levelVal)
            stack = newStack
        return res
        