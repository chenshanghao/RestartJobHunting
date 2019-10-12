class MyQueue:
    def __init__(self):
        self.first = []
        self.second = []

    def put(self, value):
        self.first.append(value)

    def peek(self):
        if not self.second:
            while self.first:
                self.second.append(self.first.pop())
        return self.second[-1]

    def pop(self):
        if not self.second:
            while self.first:
                self.second.append(self.first.pop())
        return self.second.pop()


