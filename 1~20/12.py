class Solution:
    def intToRoman(self, num):
        roman_list = [('IV', 'IX'), ('XL', 'XC'),('CD', 'CM')]
        index = 0
        roman = ""
        while num > 0 and index < 3:
            number = num % 10
            temp = ""
            if number == 4:
                temp = roman_list[index][0]
            elif number == 9:
                temp = roman_list[index][1]
            else:
                if number < 4:
                    for i in range(number):
                        temp += roman_list[index][0][0]
                else:
                    temp = roman_list[index][0][1]
                    for i in range(number - 5):
                        temp += roman_list[index][0][0]
            roman = temp + roman
            num //= 10
            index += 1
        if num != 0:
            # 1000 ~ 3999
            for i in range(num):
                roman = 'M' + roman
        return roman
