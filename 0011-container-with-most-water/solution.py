class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        ret = 0
        while l < r:
            tmp = min(height[l], height[r]) * (r-l)
            if tmp > ret:
                ret = tmp
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ret

