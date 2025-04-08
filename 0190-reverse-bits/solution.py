class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for i in range(31, -1, -1):
            ret += n//2**i * 2**(31-i)
            n = n % 2**i
            
        return ret


