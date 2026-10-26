class RLEIterator:

    def __init__(self, encoding: list[int]):
        self.encoding_iter = iter(encoding)
        self.exhausted = False
        self.curr_val = None
        self.curr_cnt = 0

    def next(self, n: int) -> int:
        while n > 0 and not self.exhausted:
            if self.curr_cnt >= n:
                self.curr_cnt -= n
                n = 0
                break
            else:
                n -= self.curr_cnt    
                try:
                    self.curr_cnt = next(self.encoding_iter)
                    self.curr_val = next(self.encoding_iter)
                except StopIteration:
                    self.exhausted = True
                    self.curr_cnt = 0
                    self.curr_val = -1
                    break
        return self.curr_val


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
