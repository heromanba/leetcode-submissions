class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        depths = [None] * len(nums)
        depths[0] = 1
        for i in range(1, len(nums)):
            curr = i
            stack = []
            while depths[curr] is None:
                stack.append(curr)
                curr = parent[curr]
            while stack:
                child = stack.pop()
                depths[child] = depths[curr] + 1
                curr = child
        weighted_sum = 0
        height = max(depths)
        for i in range(len(nums)):
            weighted_sum += nums[i] * (height-depths[i]+1)
        return weighted_sum

