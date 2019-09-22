"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root or not root.left:
            return root
        levelStack = [root.left, root.right]
        while levelStack:
            newLevelStack = []
            lengthOfLevelStack = len(levelStack)
            for i in range(lengthOfLevelStack):
                if i < lengthOfLevelStack - 1:
                    levelStack[i].next = levelStack[i + 1]
                if levelStack[i].left:
                    newLevelStack.append(levelStack[i].left)
                    newLevelStack.append(levelStack[i].right)
            levelStack = newLevelStack
        return root
        