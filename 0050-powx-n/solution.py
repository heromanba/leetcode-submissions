class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def calc(base, power):
            if power==0:return 1
            if power==1:return base
            if power==2: return base*base
            ret = calc(base, power//2)
            ret = ret*ret
            if power%2==1:
                ret = ret*x
            return ret
        ret = calc(x, abs(n))
        if n < 0:
            ret = 1/ret
        return ret
        
