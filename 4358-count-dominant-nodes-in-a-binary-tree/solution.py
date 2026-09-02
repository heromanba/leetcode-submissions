# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        # post order traversal
        stack = []
        curr = {'node': root, 'max_subtree_v': 0}
        last_visited = {'node': None, 'max_subtree_v': 0}

        num_dominate_node = 0
        while len(stack) > 0 or curr['node'] is not None:
            if curr['node'] is None:
                if stack[-1]['node'].right is None or \
                    stack[-1]['node'].right == last_visited['node']:
                    last_visited = stack.pop()
                    
                    if last_visited['node'].val >= last_visited['max_subtree_v']:
                        num_dominate_node += 1
                    if len(stack) > 0:
                        # populate max subtree value to parent
                        stack[-1]['max_subtree_v'] = max(
                            last_visited['node'].val,
                            last_visited['max_subtree_v'],
                            stack[-1]['max_subtree_v']
                        )
                else:
                    curr = {
                        'node': stack[-1]['node'].right, 
                        'max_subtree_v': 0
                    }
            else:
                stack.append(curr)
                curr = {
                    'node': curr['node'].left, 
                    'max_subtree_v': 0
                }
        return num_dominate_node

                    

