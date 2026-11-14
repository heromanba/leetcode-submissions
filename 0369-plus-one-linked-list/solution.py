# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        reversed_head = self.reverse(head)
        carries = False
        curr = reversed_head
        while True:
            if curr is reversed_head:
                plus_one = curr.val + 1
            else:
                plus_one = curr.val
            if carries:
                plus_one += 1
            if plus_one >= 10:
                curr.val = plus_one - 10
                carries = True
            else:
                curr.val = plus_one
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

