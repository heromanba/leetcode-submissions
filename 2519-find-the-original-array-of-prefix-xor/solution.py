class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ret = [pref[0]] * len(pref)
        for i in range(1, len(pref)):
            m = pref[i-1]
            n = pref[i]
            ret[i] = n^m
        return ret
