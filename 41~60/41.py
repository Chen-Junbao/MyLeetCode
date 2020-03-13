#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums):
        length = len(nums)

        if length == 0:
            return 1
        
        for i in range(length):
            while nums[i] > 0 and nums[i] <= length and nums[i] != i + 1:
                    if nums[nums[i] - 1] == nums[i]:
                        break
                    temp = nums[nums[i] - 1]
                    nums[nums[i] - 1] = nums[i]
                    nums[i] = temp
        
        for i in range(length):
            if nums[i] != i + 1:
                return i + 1
        
        return length + 1

# @lc code=end

