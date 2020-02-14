class Solution:
    def lengthOfLongestSubstring(self, s):
        maxLength = 0
        flag = []
        begin = 0
        length = len(s)
        i = 0
        while i < length:
            if s[i] in flag:
                index = s.index(s[i], begin)
                begin = index + 1
                flag[:] = s[begin: i+1]
            else:
                flag.append(s[i])
                if len(flag) > maxLength:
                    maxLength = len(flag)
            i += 1
        
        return maxLength
