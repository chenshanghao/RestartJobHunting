class MultiStack:

    def __init__(self, stacksize):
        self.numstacks = 3
        self.array = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * numstacks
        self.stacksize = stacksize

    # Return True if and only if stack is empty
    def IsEmpty(self, stacknum):
        return self.sizes[stacknum] == 0

    # Return True if and only if stack is full
    def IsFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    # Return the Top index of the stack
    def IndexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1

    # Add an item to the top of the stack
    def Push(self, item, stacknum):
        if self.IsFull(stacknum):
            raise Exception('Stack is Full')
        self.sizes[stacknum] += 1
        self.array[self.IndexOfTop(stacknum)] = item

    # Remove the top item from the stack
    def Pop(self, stacknum):
        if IsEmpty(stacknum):
            raise Exception('Stack is Empty')
        value = self.array[self.IndexOfTop(stacknum)]
        self.array[self.IndexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value

    # Return the top of the stack
    def Peek(self, stacknum):
        if IsEmpty(stacknum):
            raise Exception('Stack is Empty')
        return self.array[self.IndexOfTop(stacknum)]

