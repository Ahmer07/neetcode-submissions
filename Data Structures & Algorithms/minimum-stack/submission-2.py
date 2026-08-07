class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_val is None:
            self.min_val = val
        if val < self.min_val:
            self.min_val = val

    def pop(self) -> None:
        v = self.stack.pop()
        if v == self.min_val:
            if self.stack:
                self.min_val = min(self.stack)
            else:
                self.min_val = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val
