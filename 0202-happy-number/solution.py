class Solution:
    def isHappy(self, n: int) -> bool:
        n_str = str(n)
        seen = { n }
        while True:
            v = 0
            for d in n_str:
                v += int(d) ** 2
            if v == 1:
                return True
            if (v in seen) and ("1" not in str(v)):
                return False
            seen.add(v)
            n_str = str(v)
