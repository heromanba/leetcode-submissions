import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.watermark = 1
        self.added_back_heap = []
        self.added_back_set = set()

    def popSmallest(self) -> int:
        if self.added_back_heap:
            smallest = heapq.heappop(self.added_back_heap)
            self.added_back_set.remove(smallest)
        else:
            smallest = self.watermark
            self.watermark+=1
        return smallest

    def addBack(self, num: int) -> None:
        if num >= self.watermark:
            return
        if num in self.added_back_set:
            return
        heapq.heappush(self.added_back_heap, num)
        self.added_back_set.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
