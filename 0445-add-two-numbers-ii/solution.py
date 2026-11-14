# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        l1_reversed = self.reverse(l1)
        l2_reversed = self.reverse(l2)
        
        curr_1 = l1_reversed
        curr_2 = l2_reversed
        carries = False
        dummy_head = ListNode()
        curr_new = dummy_head
        while curr_1 or curr_2:
            if carries:
                val = 1
            else:
                val = 0
            if curr_1:
                val += curr_1.val
                curr_1 = curr_1.next
            if curr_2:
                val += curr_2.val
                curr_2 = curr_2.next
            # print(val)
            new_node = ListNode()
            if val >= 10:
                new_node.val = val-10
                carries = True
            else:
                new_node.val = val
                carries = False
            curr_new.next = new_node
            curr_new = curr_new.next
        if carries:
            new_node = ListNode(val=1)
            curr_new.next = new_node
        return self.reverse(dummy_head.next)

    
    def reverse(self, head):
        original_head = head
        while original_head.next:
            tmp = original_head.next.next
            original_head.next.next = head
            head = original_head.next
            original_head.next = tmp
        return head
