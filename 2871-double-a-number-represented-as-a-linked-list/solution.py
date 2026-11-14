# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_head = self.reverse(head)
        curr = reversed_head
        carries = False
        while True:
            doubled = curr.val * 2
            if carries:
                doubled += 1
            if doubled >= 10:
                curr.val = doubled-10
                carries = True
            else:
                curr.val = doubled
                carries = False
            if not curr.next:
                break
            curr = curr.next
        if carries:
            curr.next = ListNode(val=1)
        return self.reverse(reversed_head)

    def reverse(self, head):
        original_head = head
        while original_head.next:
            tmp = original_head.next.next
            original_head.next.next = head
            head = original_head.next
            original_head.next = tmp
        return head
