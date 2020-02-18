class Solution:
    def romanToInt(self, s):
        roman_list = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        num = 0
        while len(s) > 1:
            a = roman_list[s[0]]
            b = roman_list[s[1]]
            if a < b:
                num += b - a
                s = s[2:]
            else:
                num += a
                s = s[1:]
        if len(s) == 1:
            num += roman_list[s[0]]
        
        return num
