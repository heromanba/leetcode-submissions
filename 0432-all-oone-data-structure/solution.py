
class Node:
    def __init__(self, prev=None, next=None, data=None):
        self.prev = prev
        self.next = next
        self.data = data


class AllOne:

    def __init__(self):
        self.freq_to_key_node = dict()
        self.key_to_freq = dict()
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail

    def inc(self, key: str) -> None:
        old_freq = 0
        new_freq = old_freq + 1
        # update frequency
        if key not in self.key_to_freq:
            self.key_to_freq[key] = 1
        else:
            old_freq = self.key_to_freq[key]
            new_freq = old_freq + 1
            self.key_to_freq[key] = new_freq
        
        # decrement old frequency
        next_node = self.head.next
        if old_freq in self.freq_to_key_node:
            old_node = self.freq_to_key_node[old_freq]
            old_node.data.remove(key)

            next_node = old_node.next
            if len(old_node.data) == 0:
                # remove old node
                self.freq_to_key_node.pop(old_freq)
                next_node.prev = old_node.prev
                old_node.prev.next = next_node
        
        # add new frequency
        if new_freq in self.freq_to_key_node:
            self.freq_to_key_node[new_freq].data.add(key)
        else:
            # add new node
            new_node = Node()

            # update linked list
            new_node.prev = next_node.prev
            new_node.next = next_node

            next_node.prev.next = new_node
            next_node.prev = new_node
            
            # update freq to key dict
            new_node.data = { key }
            self.freq_to_key_node[new_freq] = new_node


    def dec(self, key: str) -> None:
        old_freq = self.key_to_freq[key]
        new_freq = old_freq - 1
        
        # remove old frequency
        old_node = self.freq_to_key_node[old_freq]
        old_node.data.remove(key)

        prev_node = old_node.prev
        if len(old_node.data) == 0:
            # remove old node
            self.freq_to_key_node.pop(old_freq)
            prev_node.next = old_node.next
            old_node.next.prev = prev_node
        
        # update frequency
        if new_freq > 0:
            self.key_to_freq[key] = new_freq
        else:
            self.key_to_freq.pop(key)
            return

        # add new frequency
        if new_freq in self.freq_to_key_node:
            self.freq_to_key_node[new_freq].data.add(key)
        else:
            # add new node
            new_node = Node()

            # update linked list
            new_node.prev = prev_node
            new_node.next = prev_node.next

            prev_node.next.prev = new_node
            prev_node.next = new_node
            
            # update freq to key dict
            new_node.data = { key }
            self.freq_to_key_node[new_freq] = new_node
        

    def getMaxKey(self) -> str:
        if self.tail.prev.data is not None:
            return str(list(self.tail.prev.data)[0])
        return ""

    def getMinKey(self) -> str:
        if self.head.next.data is not None:
            return str(list(self.head.next.data)[0])
        return ""
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
