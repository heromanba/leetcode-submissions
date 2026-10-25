import random
import bisect
class RandomizedCollection:

    def __init__(self):
        self.val_dict = dict()
        self.val_list = []
        self.val_ptr = 0

    def insert(self, val: int) -> bool:
        already_exists = val in self.val_dict
        if self.val_ptr >= len(self.val_list):
            self.val_list.append(val)
        else:
            self.val_list[self.val_ptr] = val
        if val in self.val_dict:
            self.val_dict[val].add(self.val_ptr)
        else:
            self.val_dict[val] = {self.val_ptr}
        self.val_ptr += 1
        # print('insert: ', val, self.val_dict, self.val_ptr, self.val_list)
        return not already_exists

    def remove(self, val: int) -> bool:
        already_exists = val in self.val_dict
        if val in self.val_dict:
            idx = self.val_dict[val].pop()
            if len(self.val_dict[val]) == 0:
                self.val_dict.pop(val)
            if idx < self.val_ptr-1:
                tail_val = self.val_list[self.val_ptr-1]
                self.val_dict[tail_val].remove(self.val_ptr - 1)
                self.val_dict[tail_val].add(idx)
                self.val_list[idx] = tail_val
            self.val_ptr -= 1
        # print('remove: ', val, self.val_dict, self.val_ptr, self.val_list)
        return already_exists

    def getRandom(self) -> int:
        # print('getRandom: ', self.val_dict, self.val_ptr, self.val_list)
        idx = random.randint(0, self.val_ptr-1)
        return self.val_list[idx]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
