# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)
        def buildTree(preorder, inorder):
            if (not preorder) or (not inorder):
                return
            root = TreeNode( preorder[0] )
            idx = inorder.index( preorder[0] )
            root.left = buildTree(preorder[1:idx+1], inorder[:idx])
            root.right = buildTree(preorder[idx+1:], inorder[idx+1:])
            return root
        return buildTree(preorder, inorder)
            
