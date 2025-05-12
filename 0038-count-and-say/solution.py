class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            num = self.countAndSay(n-1)
            i = 0
            j = i
            ret = ""
            while True: 
                start = num[i]
                cnt = 0
                while j<len(num) and start == num[j]:
                    cnt += 1
                    j += 1
                ret += str(cnt) + start
                if j >= len(num):
                    break
                else:
                    i = j
            return ret
