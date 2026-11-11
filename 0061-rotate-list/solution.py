# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head:
            return
        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next
        k = k % n
        slow = head
        fast = head
        i = 0
        while fast.next:
            if i < k:
                fast = fast.next
            else:
                fast = fast.next
                slow = slow.next
            i += 1
        fast.next = head
        head = slow.next
        slow.next = None
        return head
