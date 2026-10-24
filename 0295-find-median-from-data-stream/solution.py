import heapq

class MedianFinder:

    def __init__(self):
        self.smaller_half = [] # max heap
        self.larger_half = [] # min heap

    def addNum(self, num: int) -> None:
        if len(self.smaller_half) == 0 or \
            (len(self.smaller_half) > 0 and -num >= self.smaller_half[0]):
            heapq.heappush(self.smaller_half, -num)
        elif len(self.larger_half) == 0 or \
            (len(self.larger_half) > 0 and num >= self.larger_half[0]):
            heapq.heappush(self.larger_half, num)
        else:
            heapq.heappush(self.smaller_half, -num)
            # print(num)
            # raise Exception("not possible")
        # print(self.smaller_half, self.larger_half)
        # rebalance
        if len(self.smaller_half) - len(self.larger_half) > 1:
            smaller_top = -heapq.heappop(self.smaller_half)
            heapq.heappush(self.larger_half, smaller_top)
        if len(self.larger_half) - len(self.smaller_half) > 0:
            larger_top = heapq.heappop(self.larger_half)
            heapq.heappush(self.smaller_half, -larger_top)

    def findMedian(self) -> float:
        if len(self.smaller_half) == len(self.larger_half):
            return (-self.smaller_half[0] + self.larger_half[0])/2
        else:
            return -self.smaller_half[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
