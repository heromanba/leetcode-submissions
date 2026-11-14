# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if left == right:
            return head
        dummy_head = ListNode(val=None)
        dummy_head.next = head
        curr_node = dummy_head
        
        prev_node = None
        left_node = None
        right_node = None
        cnt = 0
        while True:
            if cnt == left-1:
                prev_node = curr_node
                left_node = curr_node.next
            if cnt == right:
                right_node = curr_node
                break
            curr_node = curr_node.next
            cnt += 1

        curr_node = left_node
        while left_node != right_node:
            tmp = curr_node.next.next
            curr_node.next.next = left_node
            left_node = curr_node.next
            curr_node.next = tmp
        prev_node.next = left_node
        return dummy_head.next
