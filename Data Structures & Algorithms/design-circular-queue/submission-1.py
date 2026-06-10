class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [None] * k
        self.frIdx = 0
        self.reIdx = 0
        self.length = 0 
        self.maxLen = k 

    def enQueue(self, value: int) -> bool:
        if self.length < self.maxLen:
            self.data[self.reIdx] = value
            self.reIdx = (self.reIdx + 1) % self.maxLen
            self.length += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.length > 0:
            self.frIdx = (self.frIdx + 1) % self.maxLen
            self.length -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        return self.data[self.frIdx] if self.length > 0 else -1
        

    def Rear(self) -> int:
        return self.data[self.reIdx-1] if self.length > 0 else -1

    def isEmpty(self) -> bool:
        return False if self.length > 0 else True
        

    def isFull(self) -> bool:
        return True if self.length == self.maxLen else False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()