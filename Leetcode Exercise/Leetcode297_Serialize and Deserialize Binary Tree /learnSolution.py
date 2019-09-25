# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

# deque 双向链表
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        # Use BFS to serialize the tree
        queue = deque([root])
        bfsOrder = []
        while queue:
            node = queue.popleft()
            bfsOrder.append(str(node.val) if node else '#')
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return ' '.join(bfsOrder)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        bfsOrder = [TreeNode(int(val)) if val != '#' else None for val in data.split()]
        root = bfsOrder[0]
        fastIndex = 1
        nodes, slowIndex = [root], 0
        while slowIndex < len(nodes):
            node = nodes[slowIndex]
            slowIndex += 1
            node.left = bfsOrder[fastIndex]
            node.right = bfsOrder[fastIndex + 1]
            fastIndex += 2
            
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return root
                
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))