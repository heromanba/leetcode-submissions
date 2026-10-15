class Solution:
    def checkValidString(self, s: str) -> bool:
        imbalance = 0
        num_star = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                imbalance += 1
            elif s[i] == ')':
                imbalance -= 1
            else:
                num_star += 1
            if imbalance < 0:
                num_star += imbalance
                if num_star < 0:
                    # print('l to r', i, num_star, imbalance)
                    return False
                imbalance = 0
            i += 1

        imbalance = 0
        num_star = 0
        i = len(s)-1
        while i >= 0:
            if s[i] == '(':
                imbalance -= 1
            elif s[i] == ')':
                imbalance += 1
            else:
                num_star += 1
            if imbalance < 0:
                num_star += imbalance
                if num_star < 0:
                    # print('r to l', i, num_star, imbalance)
                    return False
                imbalance = 0
            i -= 1
        return True

