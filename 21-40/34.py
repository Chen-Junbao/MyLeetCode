class Solution:
    def searchRange(self, nums, target):
        length = len(nums)
        if length == 0:
            return [-1, -1]
        if length == 1:
            if nums[0] == target:
                return [0, 0]
            return [-1, -1]
        left = 0
        right = length - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid - 1
                right = mid + 1
                while left >= 0 and nums[left] == target:
                    left -= 1
                while right < length and nums[right] == target:
                    right += 1

                return [left + 1, right - 1]

        if nums[left] == target:
            while left >= 0 and nums[left] == target:
                left -= 1
            while right < length and nums[right] == target:
                right += 1

            return [left + 1, right - 1]
        return [-1, -1]
