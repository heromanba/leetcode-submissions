class Solution {
    public void solve(char[][] board) {
        
        for(int i=0; i<board.length; i++)
            dfs(board, i, 0, 'Y');
        for(int i=0; i<board.length; i++)
            dfs(board, i, board[0].length-1, 'Y');
        
        for(int j=0; j<board[0].length; j++)
            dfs(board, 0, j, 'Y');
        for(int j=0; j<board[0].length; j++)
            dfs(board, board.length-1, j, 'Y');
        
        for(int i=1; i<board.length-1; i++)
            for(int j=1; j<board[0].length-1; j++)
                dfs(board, i, j, 'X');
        
        for(int i=0; i<board.length; i++)
            for(int j=0; j<board[0].length; j++)
                if(board[i][j]=='Y')
                    board[i][j]='O';
    }
    
    private void dfs(char[][] board, int i, int j, char val) {
        if(i<0||j<0||i>board.length-1||j>board[0].length-1)
            return;
        if(board[i][j]!='O')
            return;
        board[i][j] = val;
        dfs(board, i-1, j, val);
        dfs(board, i+1, j, val);
        dfs(board, i, j-1, val);
        dfs(board, i, j+1, val);
    }
}
