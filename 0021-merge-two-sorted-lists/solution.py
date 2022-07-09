# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (not l2):
            return l1 or l2
        new_l = None
        cur_l = None
        l1_cur = l1
        l2_cur = l2
        while l1_cur and l2_cur:
            if l1_cur.val <= l2_cur.val:
                tmp_l1_cur = l1_cur.next
                l1_cur.next = None
                cur_l_next = l1_cur
                l1_cur = tmp_l1_cur
            else:
                tmp_l2_cur = l2_cur.next
                l2_cur.next = None
                cur_l_next = l2_cur
                l2_cur = tmp_l2_cur
            if new_l is None:
                new_l = cur_l_next
            if cur_l is None:
                cur_l = cur_l_next
            else:
                cur_l.next = cur_l_next
                cur_l = cur_l.next
        if l1_cur:
            cur_l.next = l1_cur
        if l2_cur:
            cur_l.next = l2_cur
        return new_l
