class HitCounter:

    def __init__(self):
        self.ts = []
        self.prefix_cnt = []

    def hit(self, timestamp: int) -> None:
        if len(self.ts) == 0:
            self.ts.append(timestamp)
            self.prefix_cnt.append(1)
        elif len(self.ts) > 0 and self.ts[-1] == timestamp:
            self.prefix_cnt[-1] += 1
        else:
            self.ts.append(timestamp)
            prev_cnt = self.prefix_cnt[-1]+1
            self.prefix_cnt.append(prev_cnt)

    def getHits(self, timestamp: int) -> int:
        lo = 0
        hi = len(self.ts)
        left_boundary = timestamp-300
        while lo < hi:
            mid = lo + (hi-lo)//2
            if self.ts[mid] < left_boundary:
                lo = mid+1
            else:
                hi = mid
        # print(lo, left_boundary, self.ts)
        if lo == len(self.ts):
            return 0
        elif self.ts[lo] == left_boundary:
            return self.prefix_cnt[-1]-self.prefix_cnt[lo]
        elif lo == 0:
            return self.prefix_cnt[-1]
        else:
            return self.prefix_cnt[-1]-self.prefix_cnt[lo-1]



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
