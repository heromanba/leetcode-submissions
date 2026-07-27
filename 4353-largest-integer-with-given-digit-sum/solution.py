class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s > n*9:
            return -1
        ret = ''
        for i in range(n):
            if s >= 9:
                ret += '9'
                s -= 9
            else:
                ret += str(s)
                s -= s
        return int(ret)
