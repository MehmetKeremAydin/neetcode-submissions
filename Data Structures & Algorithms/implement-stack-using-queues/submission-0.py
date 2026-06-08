class MyStack:

    def __init__(self):
        self.storage = deque()

    def push(self, x: int) -> None:
        self.storage.append(x)
        
    def pop(self) -> int:
        i = 0
        while i < len(self.storage)-1:
            self.storage.append(self.storage.popleft())
            i += 1
        return self.storage.popleft()
        

    def top(self) -> int:
        i = 0
        while i < len(self.storage):
            last = self.storage.popleft()
            self.storage.append(last)
            i += 1
        return last
        

    def empty(self) -> bool:
        return not self.storage
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()