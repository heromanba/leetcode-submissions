import heapq

class StockPrice:

    def __init__(self):
        self.ts_to_idx = dict()
        self.prices = []
        self.latest_ts = float('-inf')
        self.min_heap = []
        self.max_heap = []

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.ts_to_idx:
            idx = self.ts_to_idx[timestamp]
            self.prices[idx] = price
        else:
            self.ts_to_idx[timestamp] = len(self.prices)
            self.prices.append(price)
            self.latest_ts = max(self.latest_ts, timestamp)
        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))
        
    def current(self) -> int:
        return self.prices[self.ts_to_idx[self.latest_ts]]

    def maximum(self) -> int:
        top_price, top_ts = self.max_heap[0]
        while top_price != -self.prices[self.ts_to_idx[top_ts]]:
            heapq.heappop(self.max_heap)
            top_price, top_ts = self.max_heap[0]
        return -top_price

    def minimum(self) -> int:
        top_price, top_ts = self.min_heap[0]
        while top_price != self.prices[self.ts_to_idx[top_ts]]:
            heapq.heappop(self.min_heap)
            top_price, top_ts = self.min_heap[0]
        return top_price
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
