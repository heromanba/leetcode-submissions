class Solution:
    def baseNRepr(self, n, base):
        rep = ""
        while n > base:
            rep += str( n % base )
            n = n // base
        if n > 0:
            return str(n) + rep
        else:
            return rep
        
    def isPalin(self, s):
        mid = len(s) // 2
        for i in range(mid):
            if s[i] != s[-i-1]:
                return False
        return True

    def isStrictlyPalindromic(self, n: int) -> bool:
        for b in range(2, n - 2 + 1):
            if not self.isPalin(self.baseNRepr(n, b)):
                return False
        return True
