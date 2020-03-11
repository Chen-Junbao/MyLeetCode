class Solution:
    def combinationSum2(self, candidates, target):
        length = len(candidates)
        if length == 0:
            return []

        combination = []

        def dfs(sum, index, ans):
            if sum == target:
                combination.append(ans[:])
                return

            for i in range(index, length):
                if sum + candidates[i] > target:
                    break

                if i != index and candidates[i - 1] == candidates[i]:
                    # exclude previous cases
                    continue

                ans.append(candidates[i])
                dfs(sum + candidates[i], i + 1, ans)
                ans.pop()

        candidates.sort()
        dfs(0, 0, [])

        return combination
