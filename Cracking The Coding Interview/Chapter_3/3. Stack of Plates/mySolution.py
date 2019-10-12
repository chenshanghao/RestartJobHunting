class StackofPlates:
    def __init__(self, capacity):
        if capacity < 1:
            raise NameError("A stack is greater than one.")
        else:
            self.capacity = capacity
        self.stacks = []

    def push(self, item):
        if self.stacks == []:
            self.stacks.append([item])
        else:
            if len(self.stacks[-1]) >= self.capacity:
                self.stacks.append([item])
            else:
                self.stacks[-1].append(item)

    def pop(self):
        if self.stacks == []:
            raise NameError("Cannot pop an empty stack")
        else:
            pop_item = self.stacks[-1][-1]
            if len(self.stacks[-1]) == 1:
                del self.stacks[-1]
            else:
                self.stacks[-1].pop()
        return pop_item

    def popAt(self, index):
        if self.stacks == []:
            raise NameError("Cannot pop an empty stack")
        elif len(self.stacks) < (index - 1):
            raise NameError("index out of range")
        else:
            pop_item = self.stacks[index - 1][-1]
            if len(self.stacks[index - 1]) == 1:
                del self.stacks[index - 1]
            else:
                self.stacks[index - 1][-1] = self.stacks[index][0]
                for i in range(index, len(self.stacks)):
                    for j in range(0, len(self.stacks[i]) - 1):
                        self.stacks[i][j] = self.stacks[i][j+1]
                    if i < len(self.stacks) - 1:
                        self.stacks[i][-1] = self.stacks[i+1][0]
                del self.stacks[-1][-1]
                # if length of stack is empty, delete it
                if len(self.stacks[-1]) == 0:
                    del self.stacks[-1]
        return pop_item
