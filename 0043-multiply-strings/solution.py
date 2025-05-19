class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
            
        to_int = lambda x: ord(x) - ord('0')

        ret = [0]*(len(num1)+len(num2))
        for j in range(len(num2)-1, -1, -1):
            for i in range(len(num1)-1, -1, -1):
                n1 = to_int(num1[i])
                n2 = to_int(num2[j])
                tmp = ret[i+j+1] + n1 * n2
                ret[i+j+1] = tmp%10
                ret[i+j] += tmp // 10
        ret = "".join([str(n) for idx, n in enumerate(ret) if not (idx==0 and n==0)])
        return ret or "0"


