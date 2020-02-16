#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str):
        length = len(str)
        if length == 1 and not (str[0] >= '0' and str[0] <= '9'):
            return 0
        valid_flag = False
        start = 0
        end = length
        for i in range(length):
            if str[i] != ' ':
                if str[i] == '+':
                    if str[i+1] >= '0' and str[i+1] <= '9':
                        # positive
                        start = i + 1
                        valid_flag = True
                        break
                    else:
                        break
                if str[i] >= '0' and str[i] <= '9':
                    # positive
                    start = i
                    valid_flag = True
                    break
                if str[i] == '-':
                    if str[i+1] >= '0' and str[i+1] <= '9':
                        # negative
                        start = i
                        valid_flag = True
                        break
                    else:
                        break
                if not (str[i] >= '0' and str[i] <= '9' or str[i] == '+' or str[i] == '-'):
                    # Invalid
                    break
        if valid_flag is not True:
            # Invalid
            return 0
        for i in range(start, length):
            if not (str[i] >= '0' and str[i] <= '9') and i != start:
                end = i
                break
        number = str[start:end]

        # check overflow
        length = len(number)
        if number[0] == '-':
            if number[1] == '0':
                start = length - 1
                for i in range(2, length - 1):
                    if number[i] != '0':
                        start = i
                        break
                number = '-' + number[start:]
                length = len(number)
            # negative
            if length > 11 or length == 11 and number[1] > '2':
                # overflow
                return -2147483648
            if length == 11 and number[1] == '2':
                limit = '2147483648'
                for i in range(2, 11):
                    if number[i] > limit[i-1]:
                        # overflow
                        return -2147483648
                    elif number[i] < limit[i-1]:
                        return int(number)
            return int(number)
        else:
            # positive
            if number[0] == '0':
                start = length - 1
                for i in range(1, length - 1):
                    if number[i] != '0':
                        start = i
                        break
                number = number[start:]
                length = len(number)
            if length > 10 or length == 10 and number[1] > '2':
                # overflow
                return 2147483647
            if length == 10 and number[0] == '2':
                limit = '2147483647'
                for i in range(1, 10):
                    if number[i] > limit[i]:
                        # overflow
                        return 2147483647
                    elif number[i] < limit[i]:
                        return int(number)
            return int(number)
# @lc code=end

