class Solution:
    def divide(self, dividend, divisor):
        # Check overflow
        limit = 2 ** 31 - 1
        if divisor == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend <= - (limit + 1):
                return limit
            else:
                return -dividend
        
        # Judge the sign of answer
        sign = 1
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            sign = -1
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor

        quotient = self.get_quotient(dividend, divisor)
        if sign == 1:
            return quotient
        return -quotient       
    
    def get_quotient(self, a, b):
        if a < b:
            # dividend is smaller than divisor
            return 0
        temp_b = b
        quotient = 1
        while temp_b << 2 < a:
            quotient <<= 2
            temp_b <<= 2
        
        return quotient + self.get_quotient(a - temp_b, b)
