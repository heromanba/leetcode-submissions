class Solution:
    def validTicTacToe(self, board: list[str]) -> bool:
        num_x = 0
        num_o = 0
        for row in board:
            for c in row:
                if c == 'O':
                    num_o += 1
                elif c == 'X':
                    num_x += 1
        if num_x < num_o:
            return False
        if num_x - num_o > 1:
            return False
        if num_x - num_o == 1:
            return not self._c_win(board, 'O')
        if num_x == num_o:
            # x cannot win
            return not self._c_win(board, 'X')
        return True
    
    def _c_win(self, board, c):
        target = c*3
        for row in board:
            if row == target:
                return True
        for i in range(3):
            if board[0][i]+board[1][i]+board[2][i] == target:
                return True
        if board[0][0]+board[1][1]+board[2][2] == target:
            return True
        if board[0][2]+board[1][1]+board[2][0] == target:
            return True
        return False

