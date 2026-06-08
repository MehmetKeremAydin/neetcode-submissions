class StockSpanner:
    def __init__(self):
        self.history = []
        self.day = 0

    def next(self, price: int) -> int:
        self.day += 1
        if not self.history:
            self.history.append((price, self.day))
            return 1
        else:
            while self.history and self.history[-1][0] <= price:
                self.history.pop()
            if self.history:
                span = self.day - self.history[-1][1]
                self.history.append((price, self.day))
                return span
            else:
                self.history.append((price, self.day))
                return self.day
            

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)