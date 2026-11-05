class StockSpanner:

    def __init__(self):
        self.data = []
        self.span = []

    def next(self, price: int) -> int:
        n = 1
        i = len(self.data)-1
        while self.data and price >= self.data[i]:
            n += self.span[i]
            i -= self.span[i]
            if i < 0:
                break
        self.data.append(price)
        self.span.append(n)
        return n



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
