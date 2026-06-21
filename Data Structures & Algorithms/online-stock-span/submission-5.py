class StockSpanner:

    def __init__(self):
        self.decrStack = []
        

    def next(self, price: int) -> int:
        if not self.decrStack:
            self.decrStack.append((price, 1))
            return 1
        else:
            rank = 1
            while self.decrStack and self.decrStack[-1][0] <= price:
                _, poppedRank = self.decrStack.pop()
                rank += poppedRank
            self.decrStack.append((price, rank))
            return rank
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)