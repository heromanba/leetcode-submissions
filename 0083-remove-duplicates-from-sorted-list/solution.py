# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr_ptr = head
        next_ptr = head.next
        while next_ptr:
            if next_ptr.val != curr_ptr.val:
                curr_ptr = next_ptr
            else:
                # skip duplicate nodes
                curr_ptr.next = next_ptr.next
            next_ptr = next_ptr.next
        return head

