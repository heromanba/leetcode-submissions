class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_str = self.int2bit_str(x)
        y_str = self.int2bit_str(y)
        
        x_len = len(x_str)
        y_len = len(y_str)
        
        if x_len > y_len:
            max_len = x_len
            y_str = (x_len - y_len) * '0' + y_str
        elif x_len < y_len:
            max_len = y_len
            x_str = (y_len - x_len) * '0' + x_str
        else:
            max_len = x_len
            pass
        
        counter = 0
        for i in range(max_len):
            if x_str[i] != y_str[i]:
                    counter += 1
        return counter
        
    def int2bit_str(self, x):
        """
        :type x: int
        :rtype: string
        """
        bit_str = ""
        while (x >= 1):
            order = x % 2
            bit_str = str(order) + bit_str
            x = x // 2
        return bit_str
