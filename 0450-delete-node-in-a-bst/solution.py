# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        sentinel = TreeNode(left=root)
        def dfs(parent, child):
            node = getattr(parent, child)
            if not node:
                return
            if (key < node.val) and node.left:
                dfs(node, "left")
            elif (key > node.val) and node.right:
                dfs(node, "right")
            elif key == node.val: 
                # found target node, 4 scenarios:
                # 1. no node.left, no node.right
                # 2. no node.left, has node.right
                # Attach node.right to parent for 1 and 2

                # 3. has node.left, no node.right
                # Attach node.left to parent

                # 4. has node.left, has node.right
                # Attach node.right.left to largest node in node.left
                # Attach node.left to node.right.left
                # Attach node.right to parent
                if (not node.left):
                    setattr(parent, child, node.right)
                else:
                    if node.right:
                        # find the largest leaf node in left
                        ptr = node.left
                        while ptr.right:
                            ptr = ptr.right
                        ptr.right = node.right.left
                        node.right.left = node.left
                        setattr(parent, child, node.right)
                    else:
                        setattr(parent, child, node.left)
        dfs(sentinel, 'left')
        return sentinel.left

