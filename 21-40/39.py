class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        combination = []

        self.get_sum(candidates, target, 0, 0, [], combination)

        return combination

    def get_sum(self, candidates, target, sum, index, ans, combination):
        i = index
        length = len(candidates)
        while i < length:
            ans.append(candidates[i])
            sum += candidates[i]

            if sum == target:
                combination.append(ans[:])
            elif sum < target:
                self.get_sum(candidates, target, sum, i, ans, combination)
            else:
                a = ans.pop()
                sum -= a
                break
            i += 1
            a = ans.pop()
            sum -= a
