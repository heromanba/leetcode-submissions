class Solution {
    public int findMaxFish(int[][] grid) {
        int ret = 0;
        for(int i=0; i<grid.length; i++) {
            for(int j=0; j<grid[0].length; j++) {
                if(grid[i][j]!=0) {
                    int tmp = dfs(grid, i, j);
                    if(tmp>ret)
                        ret = tmp;
                }
            }
        }
        return ret;
    }
    
    private int dfs(int[][] grid, int i, int j) {
        if(i<0||j<0||i>grid.length-1||j>grid[0].length-1)
            return 0;
        if(grid[i][j]==0)
            return 0;
        int ret = grid[i][j];
        grid[i][j] = 0;
        ret += dfs(grid, i-1, j);
        ret += dfs(grid, i+1, j);
        ret += dfs(grid, i, j-1);
        ret += dfs(grid, i, j+1);
        return ret;
    }
}
