class MinStack:

    def __init__(self):
        self.stack = []
        self.mono = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if len(self.mono) == 0 or value <= self.mono[-1]:
            self.mono.append(value)

    def pop(self) -> None:
        val = self.stack.pop()
        if len(self.mono) > 0 and val == self.mono[-1]:
            self.mono.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mono[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
