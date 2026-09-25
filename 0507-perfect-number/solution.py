class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        div_sum = 0
        for i in range(1, math.floor(num**0.5)+1):
            if num%i==0:
                div_sum += (i+num//i)
        div_sum -= num
        return div_sum == num
