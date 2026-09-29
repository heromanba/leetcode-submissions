class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        i = 0
        j = 0
        left = [None] * len(skill)
        while i < len(skill) and j < len(station):
            if skill[i] == station[j]:
                left[i] = j
                i += 1
            j += 1
        
        i = len(skill) - 1
        j = len(station) - 1
        right = [None] * len(skill)
        while i > 0 and j > 0:
            if skill[i] == station[j]:
                right[i] = j
                i -= 1
            j -= 1
        
        ret = 0
        for i in range(len(skill)-1):
            ret = max(ret, right[i+1]-left[i])
        return ret

