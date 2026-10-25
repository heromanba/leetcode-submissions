class RandomizedSet:

    def __init__(self):
        self.val_dict = dict()
        self.val_list = []
        self.val_ptr = 0

    def insert(self, val: int) -> bool:
        # print('insert: ', val, self.val_dict)
        if val in self.val_dict:
            return False
        else:
            if self.val_ptr >= len(self.val_list):
                # list is full
                self.val_list.append(val)
            else:
                # list not full
                self.val_list[self.val_ptr] = val
            self.val_dict[val] = self.val_ptr
            self.val_ptr += 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.val_dict:
            return False
        else:
            idx = self.val_dict[val]
            self.val_dict.pop(val) # remove val
            # print('remove: ', val, self.val_dict)
            if idx < self.val_ptr-1:
                self.val_list[idx] = self.val_list[self.val_ptr-1]
                self.val_dict[self.val_list[idx]] = idx # update idx for tail
            self.val_ptr -= 1
            return True

    def getRandom(self) -> int:
        idx = random.randint(0, self.val_ptr-1)
        return self.val_list[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
