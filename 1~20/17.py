class Solution:
    tel_num = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
    def letterCombinations(self, digits):
        ans = []
        self.getCharCombination(digits, "", ans)

        return ans
    def getCharCombination(self, digits, str, ans):
        if len(digits) == 0:
            return
        for c in self.tel_num[digits[0]]:
            if len(digits) == 1:
                ans.append(str + c)
            else:
                self.getCharCombination(digits[1:], str + c, ans)
