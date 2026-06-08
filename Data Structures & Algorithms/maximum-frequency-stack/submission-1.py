class FreqStack:
    def __init__(self):
        self.freqStacks = []
        self.hist = {}
        self.curMax = 0

    def push(self, val: int) -> None:
        self.hist[val] = self.hist.get(val, 0) + 1
        if len(self.freqStacks) < self.hist[val]:
            self.freqStacks.append([])
        self.freqStacks[self.hist[val]-1].append(val)
        self.curMax = max(self.curMax, self.hist[val])

    def pop(self) -> int:
        answer = self.freqStacks[self.curMax-1].pop()
        if len(self.freqStacks[self.curMax-1]) == 0:
            self.curMax -= 1
        self.hist[answer] -= 1
        return answer
        
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()