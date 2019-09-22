# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        level = [root]
        evenFlag = False
        while level:
            newLevel = []
            levelVal = []
            for node in level:
                levelVal.append(node.val)
                if node.left:
                    newLevel.append(node.left)
                if node.right:
                    newLevel.append(node.right)
            if evenFlag:
                res.append(levelVal[::-1])
                evenFlag = False
            else:
                res.append(levelVal)
                evenFlag = True   
            level = newLevel
        return res
                