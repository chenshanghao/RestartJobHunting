class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minStack = []
        self.minVal = float('inf')
        

    def push(self, x: int) -> None:
        if x < self.minVal:
            self.minVal = x
        self.minStack.append([x, self.minVal])

        

    def pop(self) -> None:
        if not self.minStack:
            return None
        res = self.minStack.pop()[0]
        if self.minStack:
            self.minVal = self.minStack[-1][1]
        else:
            self.minVal = float('inf')
        return res
        

    def top(self) -> int:
        if not self.minStack:
            return None
        return self.minStack[-1][0]
        

    def getMin(self) -> int:
        if not self.minStack:
            return None
        return self.minStack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()