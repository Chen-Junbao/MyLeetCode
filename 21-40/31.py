class Solution:
    def nextPermutation(self, nums):
        length = len(nums)
        if length < 2:
            return nums

        i = length - 2  # smaller value
        j = i + 1
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1
        if i == -1:
            # nums is descending
            nums[::] = nums[::-1]
            return nums

        # find the value which is just bigger than nums[i]
        k = length - 1  # bigger value
        while k > i and nums[i] >= nums[k]:
            k -= 1
        temp = nums[k]
        nums[k] = nums[i]
        nums[i] = temp

        nums[j:length] = nums[j:length][::-1]

        return nums
