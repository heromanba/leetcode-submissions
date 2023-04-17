# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = ListNode()
        bigger_head = ListNode()
        less_ptr = less_head
        bigger_ptr = bigger_head
        ptr = head
        while ptr:
            ptr_next = ptr.next
            if ptr.val < x:
                less_ptr.next = ptr
                less_ptr = ptr
            else:
                bigger_ptr.next = ptr
                bigger_ptr = ptr
            ptr.next = None
            ptr = ptr_next
        less_ptr.next = bigger_head.next
        return less_head.next
