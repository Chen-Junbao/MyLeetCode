class Solution:
    def reverse(self, x):
        # number to string
        s = '%d' % x
        if s[0] == '-':
            # negative
            reverse = s[1:][::-1]
            if reverse[0] == '0' and len(reverse) != 1:
                for i in range(len(reverse)):
                    if reverse[i] != '0':
                        reverse = reverse[i:]
                        break
            reverse = '-' + reverse
            limit = '2147483648'
            if len(reverse) > 11 or len(reverse) == 11 and reverse[1] > '2':
                # overflow
                return 0
            if len(reverse) == 11 and reverse[1] == '2':
                for i in range(2, 11):
                    if reverse[i] > limit[i-1]:
                        # overflow
                        return 0
                    elif reverse[i] < limit[i-1]:
                        break
            return reverse
        else:
            # positive
            reverse = s[::-1]
            if reverse[0] == '0' and len(reverse) != 1:
                for i in range(len(reverse)):
                    if reverse[i] != '0':
                        reverse = reverse[i:]
                        break
            limit = '2147483647'
            if len(reverse) > 10 or len(reverse) == 10 and reverse[0] > '2':
                # overflow
                return 0
            if len(reverse) == 10 and reverse[0] == '2':
                for i in range(1, 10):
                    if reverse[i] > limit[i]:
                        # overflow
                        return 0
                    elif reverse[i] < limit[i]:
                        break
            return reverse
