class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            tmp = set()
            for n in board[i]:
                if n != '.':
                    if n in tmp:
                        # print(i, n, tmp)
                        return False
                    else:
                        tmp.add(n)
        for j in range(9):
            tmp = set()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in tmp:
                        return False
                    else:
                        tmp.add(board[i][j])
        for i in range(3):
            for j in range(3):
                tmp = set()
                for r in range(3):
                    for l in range(3):
                        n = board[3*i+r][3*j+l]
                        if n != '.':
                            if n in tmp:
                                return False
                            else:
                                tmp.add(n)
        return True
