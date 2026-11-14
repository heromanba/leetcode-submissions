# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: ListNode | None):
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n+=1
        self.n = n
        self.head = head

    def getRandom(self) -> int:
        i = random.randint(0, self.n-1)
        curr = self.head
        while i > 0:
            curr = curr.next
            i -= 1
        return curr.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
