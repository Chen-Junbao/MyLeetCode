#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums, target):
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            if nums[0] >= target:
                return 0
            return 1

        left = 0
        right = length - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if nums[left] < target:
            return left + 1
        return left


# @lc code=end

