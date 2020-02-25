class Solution:
    def removeDuplicates(self, nums):
        length = len(nums)
        if length == 0:
            return 0
        
        left = 0
        right = 1
        while right < length:
            while right < length and nums[left] == nums[right]:
                right += 1
            if right < length:
                # find the first different value
                left += 1
                nums[left] = nums[right]
                right += 1
        
        return left + 1
