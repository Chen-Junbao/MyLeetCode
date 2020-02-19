#
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []

        length = len(nums)
        i = 0
        while i < length - 2:
            # two pointers
            j = i + 1
            k = length - 1
            while j < k:
                ans = nums[i] + nums[j] + nums[k]
                if ans == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif ans > 0:
                    # nums[k] is too large
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif ans < 0:
                    # nums[j] is too small
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
            
            while i < length - 2 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        
        return result
