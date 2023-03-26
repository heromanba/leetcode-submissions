class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        for i in range(1, len(s)+1):
            if s[-i] != " ":
                for j in range(i, len(s)+1):
                    if s[-j] != " ":
                        l += 1
                    else:
                        break
                return l
        return 0

            

