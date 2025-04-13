# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
        a b
        | |
head -> 1-2-3-4

        b a
        | |
head -> 2-1-3-4

            a b
            | |
head -> 2-1-3-4

head -> 2-1-4-3
"""
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # < 2 nodes
        if not head or not head.next:
            return head
        # >= 2 nodes
        a = head
        b = head.next
        # sentinel
        start = ListNode(0, head) 
        prev = start
        while True:
            # swap a and b
            a.next = b.next
            b.next = a
            prev.next = b
            # move to next pair
            if a.next and a.next.next:
                prev = a
                b = a.next.next
                a = a.next
            else:
                # stop if no more pair
                break   
                
        return start.next
