class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        pts = sorted(points, key=lambda x: x[0])
        max_inter = 0
        for i in range(len(pts) - 1):
            inter = pts[i+1][0] - pts[i][0]
            if inter > max_inter:
                max_inter = inter
        return max_inter
