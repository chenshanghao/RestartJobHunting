class LRUCache(object):
    class LRUNode:
        def __init__(self, key, value):
            self.prev = None
            self.next = None
            self.key = key
            self.value = value

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.map = dict()
        self.listHead = LRUCache.LRUNode(-1, -1)
        self.listTail = LRUCache.LRUNode(-1, -1)
        self.listHead.next = self.listTail
        self.listTail.prev = self.listHead
        self.capacity = capacity
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def appendNode(self, newNode):
        lastNode = self.listTail.prev
        lastNode.next = newNode
        newNode.prev = lastNode
        newNode.next = self.listTail
        self.listTail.prev = newNode    

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            cur = self.map[key]
            self.removeNode(cur)
            self.appendNode(cur)
            return cur.value
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity <= 0:
            return
        if key in self.map:
            oldNode = self.map[key]
            self.removeNode(oldNode)
            oldNode.value = value
            self.appendNode(oldNode)
        else:
            if len(self.map) >= self.capacity:
                delNode = self.listHead.next
                self.removeNode(delNode)
                del self.map[delNode.key]
            newNode = LRUCache.LRUNode(key, value)
            self.appendNode(newNode)
            self.map[key] = newNode
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)