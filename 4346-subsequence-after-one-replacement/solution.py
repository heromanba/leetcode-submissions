class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 1:
            return True

        prefix_sub = [float('inf')] * len(s)
        suffix_sub = [float('-inf')] * len(s)

        i=0
        j=0
        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                prefix_sub[i] = j
                i += 1
                j += 1
            else:
                j += 1
        
        i=len(s)-1
        j=len(t)-1
        while i >= 0 and j >= 0:
            if s[i] == t[j]:
                suffix_sub[i] = j
                i -= 1
                j -= 1
            else:
                j -= 1
        print(prefix_sub, suffix_sub)
        for i in range(len(s)):
            if prefix_sub[i] <= suffix_sub[i]:
                return True
            elif i == 0 and i+1<len(s) and suffix_sub[i+1] > 0:
                return True
            elif i == len(s)-1 and i-1 >=0 and prefix_sub[i-1] < len(t)-1:
                return True
            elif 0 <= i-1 and i+1 < len(s) and prefix_sub[i-1] < suffix_sub[i+1]-1:
                return True
        return False
