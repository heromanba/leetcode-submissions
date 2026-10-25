class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1]*k
        self.size = 0
        self.capacity = k
        self.start = 0
        self.end = -1

    def enQueue(self, value: int) -> bool:
        if self.size < self.capacity:
            self.end = (self.end+1)%len(self.queue)
            self.queue[self.end] = value
            self.size += 1
            # print('enqueue: ', value, self.start, self.end, self.size, self.queue)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.size > 0:
            self.start = (self.start+1)%len(self.queue)
            self.size -= 1
            return True
        else:
            return False
        

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[self.start]

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[self.end]
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
