# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        dummy_head = ListNode()
        dummy_head.next = head
        prev = dummy_head
        start = head
        while True:
            while start and start.next and start.val != start.next.val:
                prev = start
                start = start.next
            if not start or not start.next:
                # end of list
                break
            end = start.next
            while end and end.next and end.val == end.next.val:
                end = end.next
            prev.next = end.next
            start = prev.next
        return dummy_head.next
