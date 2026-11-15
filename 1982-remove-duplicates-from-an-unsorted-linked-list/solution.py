# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        seen_val = set()
        dupe_val = set()
        curr = head
        while curr:
            if curr.val not in seen_val:
                seen_val.add(curr.val)
            else:
                dupe_val.add(curr.val)
            curr = curr.next
        dummy_head = ListNode()
        dummy_head.next = head
        prev = dummy_head
        curr = head
        while curr:
            if curr.val in dupe_val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy_head.next
