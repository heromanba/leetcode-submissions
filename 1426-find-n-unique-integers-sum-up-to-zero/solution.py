class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 0:
            half = n // 2
            res = []
            for i in range(1, half + 1):
                res.append(i)
                res.append(-i)
        else:
            half = (n + 1) // 2
            res = []
            res.append(0)
            for i in range(1, half):
                res.append(i)
                res.append(-i)
        return res
