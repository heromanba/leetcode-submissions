class Solution {
    
    private int cnt = 1;
    
    public int countSubIslands(int[][] grid1, int[][] grid2) {
        
        for(int i=0; i<grid2.length; i++) {
            for(int j=0; j<grid2[0].length; j++) {
                if(grid2[i][j]==1) {
                    cnt++;
                    dfs(grid2, i, j);
                }
            }
        }
        
        Map<Integer, Boolean> tmp = new HashMap<>(cnt-1);
        for(int i=2; i<=cnt; i++) {
            tmp.put(i, true);
        }
        for(int i=0; i<grid1.length; i++) {
            for(int j=0; j<grid1[0].length; j++) {
                if((grid2[i][j]!=0)&&(grid1[i][j]!=1)) {
                    tmp.put(grid2[i][j], false);
                }
            }
        }
        int ret = 0;
        for(Map.Entry<Integer, Boolean> entry: tmp.entrySet())
            if(entry.getValue())
                ret++;
        return ret;
        
    }
    
    public void dfs(int[][] grid, int i, int j) {
        if(i<0||i>=grid.length||j<0||j>=grid[0].length)
            return;
        if(grid[i][j]==0||grid[i][j]!=1)
            return;
        grid[i][j]=cnt;
        dfs(grid, i-1, j);
        dfs(grid, i+1, j);
        dfs(grid, i, j-1);
        dfs(grid, i, j+1);
    }
}
