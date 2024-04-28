class Solution {
    public int closedIsland(int[][] grid) {
        for(int i=0; i<grid.length; i++)
            dfs(grid, i, 0);
        for(int i=0; i<grid.length; i++)
            dfs(grid, i, grid[0].length-1);
        
        for(int j=0; j<grid[0].length; j++)
            dfs(grid, 0, j);
        for(int j=0; j<grid[0].length; j++)
            dfs(grid, grid.length-1, j);
        
        int ret = 0;
        for(int i=0; i<grid.length; i++) {
            for(int j=0; j<grid[0].length; j++) {
                if(grid[i][j]==0) {
                    ret++;
                    dfs(grid, i, j);
                }
            }
        }
        return ret;
                
    }
    
    private void dfs(int[][] grid, int i, int j) {
        if(i<0||j<0||i>grid.length-1||j>grid[0].length-1)
            return;
        if(grid[i][j]==1)
            return;
        grid[i][j]=1;
        dfs(grid, i-1, j);
        dfs(grid, i+1, j);
        dfs(grid, i, j-1);
        dfs(grid, i, j+1);
    }
}
