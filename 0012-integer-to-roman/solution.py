class Solution:

    mapping = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
    }
    subtractive = {
        4: "IV",
        9: "IX",
        40: "XL",
        90: "XC",
        400: "CD",
        900: "CM",
    }
    def intToRoman(self, num: int) -> str:
        ret = ''
        while num > 0:
            if str(num)[0] not in '49':
                tmp = None
                for n in [1000, 500, 100, 50, 10, 5, 1]:
                    if num - n >= 0:
                        tmp = n
                        break
                ret += self.mapping[tmp]
                num -= tmp
            else:
                tmp = None
                for n in [900, 400, 90, 40, 9, 4]:
                    if num - n >= 0:
                        tmp = n
                        break
                ret += self.subtractive[tmp]
                num -= tmp
        return ret
            
            

