"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        if not root or not p:
            return None
        
        cur, last = root, None
        while cur != p:
            if cur.val < p.val:
                cur = cur.right
            else:
                last = cur
                cur = cur.left
        if cur.right:
            cur = cur.right
            while cur.left:
                cur = cur.left
            return cur
        else:
            return last