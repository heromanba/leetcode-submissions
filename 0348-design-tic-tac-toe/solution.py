class TicTacToe:

    def __init__(self, n: int):
        self.board = [
            [0 for _ in range(n)]
            for _ in range(n)
        ]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        # scan all cols for the same row
        all_same_player = True
        for j in range(self.n):
            if self.board[row][j] != player:
                all_same_player = False
                break
        if all_same_player:
            return player

        # scan all rows for the same col
        all_same_player = True
        for i in range(self.n):
            if self.board[i][col] != player:
                all_same_player = False
                break
        if all_same_player:
            return player
        
        # check diagonal
        all_same_player = True
        if row == col:
            for i in range(self.n):
                if self.board[i][i] != player:
                    all_same_player = False
                    break
            if all_same_player:
                return player

        # check diagonal
        all_same_player = True
        if row + col == self.n-1:
            for i in range(self.n-1, -1, -1):
                if self.board[i][self.n-1-i] != player:
                    all_same_player = False
                    break
            if all_same_player:
                return player

        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
