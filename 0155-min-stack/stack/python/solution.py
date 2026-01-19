class MinStack:
    def __init__(self):
        self.stack = [] # Stack of Tuples (value, minimum)

    def push(self, val: int) -> None:
        cur_min = val
        if self.stack:
            cur_min = min(cur_min, self.stack[-1][1])
        self.stack.append((val, cur_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
