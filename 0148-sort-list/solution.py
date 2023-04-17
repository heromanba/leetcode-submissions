# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        array = []
        ptr = head
        while ptr:
            array.append(ptr.val)
            ptr = ptr.next
        array = sorted(array)
        ptr = head
        cnt = 0
        while ptr:
            ptr.val = array[cnt]
            ptr = ptr.next
            cnt += 1
        return head
