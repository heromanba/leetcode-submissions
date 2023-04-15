# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        created = dict()
        parent = dict()
        for parent_v, child_v, is_left in descriptions:
            parent[child_v] = parent_v
            if parent_v not in parent:
                parent[parent_v] = None
            if parent_v in created:
                parent_node = created[parent_v]
            else:
                parent_node = TreeNode(parent_v)
                created[parent_v] = parent_node
            if child_v in created:
                child_node = created[child_v]
            else:
                child_node = TreeNode(child_v)
                created[child_v] = child_node
            if is_left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
        root_v = None
        for k, v in parent.items():
            if v is None:
                root_v = k
                break
        return created[root_v]
