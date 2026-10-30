from copy import deepcopy

class Solution:

    def _get_num_live_neighbors(self, board, i, j):
        n = 0
        offsets = [(-1,-1),(-1,0),(0,-1),(0,1),(1,0),(1,1),(-1,1),(1,-1)]
        for x,y in offsets:
            if 0 <= i+x < len(board) and 0 <= j+y < len(board[0]):
                if board[i+x][j+y] == 1:
                    n+=1
        return n

    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        prev = deepcopy(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                n = self._get_num_live_neighbors(prev, i, j)
                if prev[i][j] == 1:
                    if n < 2:
                        board[i][j] = 0
                    elif n == 2 or n == 3:
                        board[i][j] = 1
                    elif n > 3:
                        board[i][j] = 0
                else:
                    if n == 3:
                        board[i][j] = 1
        
