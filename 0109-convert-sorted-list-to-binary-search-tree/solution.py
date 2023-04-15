# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        array = []
        
        while head:
            array.append(head.val)
            head = head.next
        def toBST(array):
            if not array:
                return
            if len(array) == 1:
                return TreeNode(array[0])
            idx = len(array) // 2
            
            root = TreeNode(array[idx])
            root.left = toBST(array[:idx])
            root.right = toBST(array[idx+1:])
            return root
        return toBST(array)







        
