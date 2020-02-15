class Solution:
    def convert(self, s, numRows):
        if s == "":
            return s
        if numRows == 1:
            return s
        if numRows >= len(s):
            return s

        length = len(s)
        arr = [[] for i in range(numRows)]
        flag = 1
        row = 0
        for i in range(length):
            arr[row].append(s[i])
            if (row == numRows-1 or row == 0) and i != 0:
                flag = -flag
            row += flag
        z_string = ""
        for i in range(numRows):
            z_string += "".join(arr[i])

        return z_string
