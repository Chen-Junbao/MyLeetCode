class Solution:
    def twoSum(self, nums, target):
        d = {}  # Key is the value of the number, value is the index of the number
        length = len(nums)
        for i in range(length):
            d[nums[i]] = i
        for i in range(length):
            value = target - nums[i]
            if value in d and d[value] != i:
                return [i, d[value]]
        return None
