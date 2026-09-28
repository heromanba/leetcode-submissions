from decimal import Decimal
class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        start = round(l**(1/k))
        if start**k != l:
            start = math.ceil(l**(1/k))
        end = round(r**(1/k))
        if end**k != r:
            end = math.floor(r**(1/k))
        return end-start+1
