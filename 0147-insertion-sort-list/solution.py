# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        dummy_head = ListNode(float('-inf'), head)
        dummy_tail = ListNode(float('inf'))

        curr_node = dummy_head
        parent_map = dict()
        while True:
            if curr_node.next:
                parent_map[curr_node.next] = curr_node
            else:
                curr_node.next = dummy_tail
                parent_map[dummy_tail] = curr_node
                break
            curr_node = curr_node.next
        
        curr_node = head
        while curr_node:
            next_node = curr_node.next
            target_node = parent_map[curr_node]
            
            in_place = True
            while target_node.val > curr_node.val:
                target_node = parent_map[target_node]
                in_place = False
            if not in_place:
                # detach
                parent_map[curr_node].next = next_node
                parent_map[next_node] = parent_map[curr_node]

                parent_map[curr_node] = target_node
                parent_map[target_node.next] = curr_node

                curr_node.next = target_node.next
                target_node.next = curr_node
            # print(curr_node.val, target_node.val, in_place)
            # print({k.val: v.val for k, v in parent_map.items()})
                    
            curr_node = next_node
        parent_map[dummy_tail].next = None
        return dummy_head.next
