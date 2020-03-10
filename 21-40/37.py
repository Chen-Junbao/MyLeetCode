class Solution:
    def solveSudoku(self, board) -> None:
        # mark the use of numbers in each row and column
        row_flag = [[0 for n in range(9)] for row in range(9)]
        col_flag = [[0 for n in range(9)] for col in range(9)]
        # mark the use of number in each block
        block_flag = [[[0 for n in range(9)]
                       for col in range(3)] for row in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row_flag[i][int(board[i][j]) - 1] = 1
                    col_flag[j][int(board[i][j]) - 1] = 1
                    block_flag[i // 3][j // 3][int(board[i][j]) - 1] = 1

        self.fill(board, row_flag, col_flag, block_flag, 0, 0)

    def fill(self, board, row_flag, col_flag, block_flag, row, col):
        if col == 9:
            col = 0
            row += 1
            if row == 9:
                return True
        if board[row][col] == '.':
            for i in range(9):
                if row_flag[row][i] == 0 and col_flag[col][i] == 0 and block_flag[row // 3][col // 3][i] == 0:
                    board[row][col] = str(i + 1)
                    row_flag[row][i] = 1
                    col_flag[col][i] = 1
                    block_flag[row // 3][col // 3][i] = 1

                    if self.fill(board, row_flag, col_flag, block_flag, row, col + 1):
                        return True

                    board[row][col] = '.'
                    row_flag[row][i] = 0
                    col_flag[col][i] = 0
                    block_flag[row // 3][col // 3][i] = 0
        else:
            return self.fill(board, row_flag, col_flag, block_flag, row, col + 1)

        return False
