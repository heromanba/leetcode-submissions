# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        head = ListNode()
        curr = head
        pq = []
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(pq, (node.val, idx, node))
        while pq:
            _, idx, node = heapq.heappop(pq)
            if node.next:
                heapq.heappush(pq, (node.next.val, idx, node.next))
            curr.next = node
            curr = curr.next
        return head.next

