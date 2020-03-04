class Solution:
    def longestValidParentheses(self, s):
        left = 0
        right = 0

        max_length = 0

        # from left to right
        length = len(s)

        cnt = 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                right += 1
            if left == right:
                cnt += left
                left = right = 0
                if cnt > max_length:
                    max_length = cnt
            elif left < right:
                cnt = 0
                left = right = 0

        # from right to left
        left = 0
        right = 0
        cnt = 0
        for c in s[::-1]:
            if c == '(':
                left += 1
            elif c == ')':
                right += 1
            if left == right:
                cnt += left
                left = right = 0
                if cnt > max_length:
                    max_length = cnt
            elif left > right:
                cnt = 0
                left = right = 0

        return max_length * 2
