# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy_head = ListNode()
        dummy_head.next = head

        prev_tail = dummy_head
        curr_head = head
        curr_tail = head
        while curr_head:
            # curr_tail move k-1 steps first
            for _ in range(k-1):
                if not curr_tail.next:
                    return dummy_head.next
                curr_tail = curr_tail.next
                
            curr_ptr = curr_head
            while curr_head is not curr_tail:
                tmp = curr_ptr.next.next
                curr_ptr.next.next = curr_head
                curr_head = curr_ptr.next
                
                curr_ptr.next = tmp

            prev_tail.next = curr_head
            
            prev_tail = curr_ptr               
            curr_head = curr_ptr.next
            curr_tail = curr_ptr.next              
            
        return dummy_head.next


