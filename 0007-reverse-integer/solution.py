class Solution:
    def reverse(self, x: int) -> int:
        tmp = []
        direction = 1 if x>0 else -1
        x = abs(x)
        while x > 0:
            tmp.append(x%10)
            x = int(x / 10)
        ret = 0
        for i in range(len(tmp)):
            ret += tmp[len(tmp)-i-1] * 10**i
        ret *= direction
        if ret > 2**31-1 or ret < -2**31:
            return 0
        return ret

