
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._move_node_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            # add new node to map
            node = Node(key, value)
            node.next = self.head
            if self.head:
                self.head.prev = node
            self.head = node
            if len(self.map) == 0:
                self.tail = node
            self.map[key] = node
            # print(self.map, self.tail, key, value)
            if len(self.map) > self.capacity:
                # pop tail
                old_tail = self.tail
                self.map.pop(old_tail.key)
                self.tail = old_tail.prev
                self.tail.next = None
        else:
            # update existing node and move to head
            node = self.map[key]
            node.val = value
            self._move_node_to_head(node)

    def _move_node_to_head(self, node):
        if node is self.head:
            return
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node is self.tail:
            # print(node, node.val, node.prev, 'update tail')
            self.tail = node.prev
        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
