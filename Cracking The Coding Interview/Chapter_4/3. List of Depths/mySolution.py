"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        reslist = []
        if not root:
            return reslist
        list_level_node = [root]
        while list_level_node:
            new_list_level_node = []
            start_node = tmp = ListNode(list_level_node[0].val)
            if list_level_node[0].left:
                new_list_level_node.append(list_level_node[0].left)
            if list_level_node[0].right:
                new_list_level_node.append(list_level_node[0].right)
            
            for node in list_level_node[1:]:
                tmp.next = ListNode(node.val)
                if node.left:
                    new_list_level_node.append(node.left)
                if node.right:
                    new_list_level_node.append(node.right)
                tmp = tmp.next
            
            reslist.append(start_node)
            list_level_node = new_list_level_node
        return reslist
            
                
            