#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
import numpy as np


class Solution:
    def longestPalindrome(self, s):
        length = len(s)
        dp = [0] * length

        reverse = s[::-1]
        max_len = 1
        index = 0  # Record the end of the palindrome string
        for i in range(length):
            for j in range(length-1, -1, -1):
                if s[i] == reverse[j]:
                    if i == 0 or j == 0:
                        dp[j] = 1
                    else:
                        dp[j] = dp[j-1] + 1
                else:
                    dp[j] = 0
                if dp[j] > max_len and s[i-dp[j]+1] == s[i]:
                    max_len = dp[j]
                    index = i

        return s[index-max_len+1:index+1]
# @lc code=end
