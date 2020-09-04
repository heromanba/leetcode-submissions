class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = float('-inf')
        for i in candies:
            if i > max_candy:
                max_candy = i
        res = []
        for i in candies:
            if i + extraCandies >= max_candy:
                res.append(True)
            else:
                res.append(False)
        return res
