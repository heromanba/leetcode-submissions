# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        # find max
        max_v = float('-inf')
        max_idx = None
        for i in range(len(nums)):
            if nums[i] > max_v:
                max_v = nums[i]
                max_idx = i
        node = TreeNode(max_v)
        if max_idx > 0:
            node.left = self.constructMaximumBinaryTree(nums[:max_idx])
        if max_idx + 1 < len(nums):
            node.right = self.constructMaximumBinaryTree(nums[max_idx+1:])
        return node
