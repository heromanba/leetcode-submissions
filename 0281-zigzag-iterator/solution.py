class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1=v1
        self.v2=v2
        self.ptr1 = 0
        self.ptr2 = 0

    def next(self) -> int:
        if self.ptr1 < len(self.v1) and (self.ptr1 <= self.ptr2 or self.ptr2 >= len(self.v2)):
            val = self.v1[self.ptr1]
            self.ptr1+=1
            return val
        if self.ptr2 < len(self.v2) and (self.ptr2 < self.ptr1 or self.ptr1 >= len(self.v1)):
            val = self.v2[self.ptr2]
            self.ptr2+=1
            return val

    def hasNext(self) -> bool:
        return self.ptr1 < len(self.v1) or self.ptr2 < len(self.v2)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
