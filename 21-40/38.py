class Solution:
    def countAndSay(self, n):
        i = 1
        ans = "1"

        while i < n:
            temp = ""
            j = 1
            length = len(ans)

            cnt = 1
            while j < length:
                if ans[j - 1] == ans[j]:
                    cnt += 1
                    j += 1
                else:
                    temp += str(cnt)
                    temp += ans[j - 1]
                    cnt = 1
                    j += 1
            
            temp += str(cnt)
            temp += ans[length - 1]
            ans = temp
            i += 1
        
        return ans
