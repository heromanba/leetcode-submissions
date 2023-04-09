class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_str = str(n)
        sum_v = sum([int(i) for i in n_str])
        prod_v = 1
        for i in n_str:
            prod_v *= int(i)
        return prod_v - sum_v
