#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        length_h = len(haystack)
        length_n = len(needle)
        i = 0
        while i + length_n <= length_h:
            sub_string = haystack[i: length_n + i]
            if sub_string == needle:
                return i
            i += 1
        return -1
# @lc code=end

