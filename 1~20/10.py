class Solution:
    def isMatch(self, s, p):
        len_s = len(s)
        len_p = len(p)

        if len_p == 0:
            # p is empty, s should also be empty
            return len_s == 0
        if len_p > 1 and p[1] == '*':
            # case: .* or [a-z]*
            if len_s == 0:
                # s is empty, * is used to replace 0 times
                return len_p == 2 or self.isMatch(s, p[2:])
            elif p[0] == s[0] or p[0] == '.':
                # multiple times or 1 time
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                # 0 times
                return self.isMatch(s, p[2:])
        else:
            # p[1] != '*'
            return len_s != 0 and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
