class FreqStack:

    def __init__(self):
        self.hist = {}
        self.heap = []
        self.opCount = 0
        

    def push(self, val: int) -> None:
        self.hist[val] = self.hist.get(val, 0) + 1
        heapq.heappush_max(self.heap, (self.hist[val], self.opCount, val))
        self.opCount += 1
        return

    def pop(self) -> int:
        elemCount, _, val = heapq.heappop_max(self.heap)
        self.hist[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()