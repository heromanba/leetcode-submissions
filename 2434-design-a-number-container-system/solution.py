import heapq

class NumberContainers:

    def __init__(self):
        self.idx_to_num = dict()
        self.num_to_idx = dict()
        self.num_idx_min_heap = dict()
        
    def change(self, index: int, number: int) -> None:
        if index not in self.idx_to_num:
            self.idx_to_num[index] = number
        else:
            old_number = self.idx_to_num[index]
            self.num_to_idx[old_number].remove(index)
            self.idx_to_num[index] = number

        if number not in self.num_to_idx:
            self.num_to_idx[number] = { index }
            self.num_idx_min_heap[number] = [ index ]
        else:
            self.num_to_idx[number].add(index)
            heapq.heappush(self.num_idx_min_heap[number], index)

    def find(self, number: int) -> int:
        if number not in self.num_to_idx or len(self.num_to_idx[number]) == 0:
            return -1
        top_idx = self.num_idx_min_heap[number][0]
        while top_idx not in self.num_to_idx[number]:
            heapq.heappop(self.num_idx_min_heap[number])
            top_idx = self.num_idx_min_heap[number][0]
        return top_idx



# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
