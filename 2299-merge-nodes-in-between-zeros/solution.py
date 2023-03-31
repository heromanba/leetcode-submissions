# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        new_curr = None

        slow = head
        fast = head.next
        sumV = 0
        while fast:
            if fast.val == 0:
                # add to new list
                if new_head is None:
                    new_head = ListNode(sumV)
                    new_curr = new_head
                else:
                    new_curr.next = ListNode(sumV)
                    new_curr = new_curr.next
                # reset sum
                sumV = 0
            sumV += fast.val
            fast = fast.next
        return new_head

