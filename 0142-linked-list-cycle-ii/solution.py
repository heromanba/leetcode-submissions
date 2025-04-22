# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        slow = head
        fast = head
        while True:
            if not fast.next:
                return
            fast = fast.next.next
            slow = slow.next
            if not fast or not slow:
                return
            if slow == fast:
                break
        fast = head
        while True:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next

