class FreqStack:
    def __init__(self):
        self.dataCount = dict()
        self.freqHeap = []
        self.time = 0

    def push(self, val: int) -> None:
        self.time+=1
        self.dataCount[val] = self.dataCount.get(val, 0) + 1
        if self.dataCount[val] == 1:
            heapq.heappush_max(self.freqHeap, (1, self.time, val))
        else:
            heapq.heappush_max(self.freqHeap, (self.dataCount[val], self.time, val))

    def pop(self) -> int:
        freq, time, val = heapq.heappop_max(self.freqHeap)
        self.dataCount[val] -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()