class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        selfDividingNums = []
        for num in range(left, right + 1):
            
            num_str_set = set(str(num))
            
            
            if '0' in num_str_set:
                continue
            
            selfDividing = True
            for digit in num_str_set:
                if num % int(digit) == 0:
                    pass
                else:
                    selfDividing = False
                    break
                    
            if selfDividing:
                selfDividingNums.append(num)
                
        return selfDividingNums
            
            
