class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        auxStack = []
        while self.stack:
            last = self.stack.pop()
            if self.stack:
                auxStack.append(last)
        while auxStack:
            self.stack.append(auxStack.pop())
        return last
        
    def peek(self) -> int:
        auxStack = []
        while self.stack:
            last = self.stack.pop()
            auxStack.append(last)
        while auxStack:
            self.stack.append(auxStack.pop())
        return last
        

    def empty(self) -> bool:
        return not self.stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()