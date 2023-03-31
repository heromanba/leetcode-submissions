class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ret = [0] * len(queries)
        for pt in points:
            for i in range(len(queries)):
                x, y, r = queries[i]
                if (pt[0] - x) ** 2 + (pt[1] - y) ** 2 <= r ** 2:
                    ret[i] += 1
        return ret

