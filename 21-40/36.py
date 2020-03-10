from collections import Counter
import numpy as np


class Solution:
    def isValidSudoku(self, board):
        board = np.asarray(board)
        for i in range(9):
            a = Counter(board[i])
            for item in a.items():
                if item[1] > 1 and item[0] != '.':
                    return False
            a = Counter(board[:, i])
            for item in a.items():
                if item[1] > 1 and item[0] != '.':
                    return False

        for row in range(3):
            for col in range(3):
                array = board[row * 3: row * 3 + 3, col * 3: col * 3 + 3]
                a = Counter(array.flatten())
                for item in a.items():
                    if item[1] > 1 and item[0] != '.':
                        return False

        return True
