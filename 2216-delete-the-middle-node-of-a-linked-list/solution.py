# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1
        if n <= 1:
            return
        prev = head
        curr = head
        i = 0
        while True:
            if i == math.floor(n/2)-1:
                prev = curr
                break
            i += 1
            curr = curr.next
        prev.next = prev.next.next
        return head
