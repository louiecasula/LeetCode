class MinStack:

    stack = []

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) > 0 and val > self.stack[len(self.stack) - 1][1]:
            self.stack.append([val, self.stack[len(self.stack) - 1][1]])
        else:
            self.stack.append([val, val])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1][0]

    def getMin(self) -> int:
        return self.stack[len(self.stack) - 1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()