class Solution:
    def countDigits(self, num: int) -> int:
        n = 0
        for d in str(num):
            if num % int(d) == 0:
                n += 1
        return n
