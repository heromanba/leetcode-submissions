class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # number to sequence
        digits = []
        while True:
            d = x % 10
            digits.append(d)
            if x < 10:
                break
            else:
                x = x // 10
        digits = digits[::-1]
        # check if digits are palindrome
        n = len(digits) // 2
        for i in range(n):
            if digits[i] != digits[-(i+1)]:
                return False
        return True

if __name__ == "__main__":
    print(Solution().isPalindrome(121))
    print(Solution().isPalindrome(-121))
    print(Solution().isPalindrome(10))
    
