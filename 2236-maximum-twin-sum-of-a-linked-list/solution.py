# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr_node = head
        ll_len = 0
        while curr_node:
            ll_len += 1
            curr_node = curr_node.next
        
        curr_node = head
        twin_sum = []
        cnt = 0
        while curr_node:
            if cnt < ll_len // 2:
                twin_sum.append(curr_node.val)
            else:
                twin_sum[ll_len // 2 - cnt - 1] += curr_node.val
            curr_node = curr_node.next
            cnt += 1
        return max(twin_sum)
