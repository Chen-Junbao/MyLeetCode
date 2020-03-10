#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start


class Solution:
    def search(self, nums, target):
        length = len(nums)
        if length == 0:
            return -1
        if length == 1:
            if nums[0] == target:
                return 0
            return -1

        left = 0
        right = length - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # find bigger value
                if nums[left] <= nums[mid]:
                    # values in [left, mid] are all smaller than target
                    left = mid + 1
                else:
                    if nums[left] > target:
                        # values in [left, mid] are not equal to target (bigger or smaller)
                        left = mid + 1
                    else:
                        right = mid - 1
            else:
                # find smaller value
                if nums[left] <= nums[mid]:
                    if nums[left] > target:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    right = mid - 1

        if nums[left] == target:
            return left
        return -1

# @lc code=end
