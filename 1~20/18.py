class Solution:
    def fourSum(self, nums, target):
        length = len(nums)
        if length == 4:
            if nums[0] + nums[1] + nums[2] + nums[3] == target:
                return [nums]
            else:
                return []

        nums.sort()
        ans = []
        i = 0
        while i < length - 3:
            value = target - nums[i]
            j = i + 1
            while j < length - 2:
                k = j + 1
                l = length - 1
                while k < l:
                    sum = nums[j] + nums[k] + nums[l]
                    if sum == value:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
                    elif sum < value:
                        # nums[k] is too small
                        k += 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                    elif sum > value:
                        # nums[l] is too large
                        l -= 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
                while j < length - 2 and nums[j] == nums[j+1]:
                    j += 1
                j += 1
            while i < length - 3 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        
        return ans
