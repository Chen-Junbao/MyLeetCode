class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        length = len(nums)
        if length == 3:
            return nums[0] + nums[1] + nums[2]
        i = 0
        min_delta = 99999
        ans = 0
        while i < length - 2:
            j = i + 1
            k = length - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    # best answer
                    return sum
                delta = abs(sum - target)
                if delta < min_delta:
                    min_delta = delta
                    ans = sum
                if sum > target:
                    # nums[k] is too large
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif sum < target:
                    # nums[j] is too small
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
            while i < length - 2 and nums[i] == nums[i+1]:
                i += 1
            i += 1
    
        return ans
