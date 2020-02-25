class Solution:
    def __init__(self):
        super().__init__()
        self.ans = []

    def generateParenthesis(self, n):
        if n == 0:
            return []
        self.getCombination(0, 0, "", n)

        return self.ans

    def getCombination(self, left, right, str, n):
        if left == n and right == n:
            self.ans.append(str)
            return
        if left < n and left >= right:
            self.getCombination(left + 1, right, str + '(', n)
        if left > right:
            self.getCombination(left, right + 1, str + ')', n)
