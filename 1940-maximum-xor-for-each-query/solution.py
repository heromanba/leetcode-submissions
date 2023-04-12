class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ret = []
        xor = 0
        for n in nums:
            xor ^= n
            ret.append(xor)
        ret = ret[::-1]
        def getReverseBinRepr(n):
            rep = [1] * maximumBit
            original_n = n
            if n == 0:
                rep[-1] = 1
            else:
                cnt = 1
                while n != 0:
                    digit = n % 2
                    if digit == 1:
                        rep[-cnt] = 0
                    else:
                        rep[-cnt] = 1
                    n = n // 2
                    cnt += 1
            ret_num = 0
            cnt = 0
            for i in range(1, len(rep)+1):
                ret_num += rep[-i] * 2**cnt
                cnt += 1
            return ret_num
        return [getReverseBinRepr(i) for i in ret]

