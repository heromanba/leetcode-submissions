class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        rev = int(str(n)[::-1])
        start = min(rev, n)
        end = max(rev, n)
        ans = 0
        for i in range(start, end+1):
            if self.check_prime(i):
                print(i)
                ans += i
        return ans
    
    def check_prime(self, n):
        if n < 2:
            return False
        for i in range(2, math.ceil(math.sqrt(n))+1):
            if i!=n and n%i == 0:
                return False
        return True
