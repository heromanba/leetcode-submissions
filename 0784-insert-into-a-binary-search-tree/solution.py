# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        sentinel = TreeNode(left=root)
        def dfs(parent, child):
            node = getattr(parent, child)
            if not node:
                setattr(parent, child, TreeNode(val))
                return    
            if val < node.val:
                dfs(node, "left")
            else:
                dfs(node, "right")
        dfs(sentinel, "left")
        return root
