class Solution {
    public int numEnclaves(int[][] grid) {
        for(int i=0,j=0; j<grid[0].length; j++) {
            dfs(grid, i, j);
        }
        for(int i=grid.length-1,j=0; j<grid[0].length; j++) {
            dfs(grid, i, j);
        }
        for(int i=0,j=0; i<grid.length; i++) {
            dfs(grid, i, j);
        }
        for(int i=0,j=grid[0].length-1; i<grid.length; i++) {
            dfs(grid, i, j);
        }
        // System.out.println("----------");
        for(int i=1; i<grid.length-1; i++) {
            for(int j=1; j<grid[0].length-1; j++) {
                // dfs(grid, i, j, true);
                if(grid[i][j]==1)
                    n+=1;
            }
        }
        return n;
    }
    
    private int n = 0;
    
    private int[][] directions = {{-1,0}, {1,0}, {0,-1}, {0,1}};
    
    private void dfs(int[][] grid, int i, int j) {
        if(grid[i][j]==0)
            return;
        if(grid[i][j]==1) {
            // System.out.println("i:"+i+"j:"+j+"g:"+grid[i][j]);
            // if(count)
            //     n+=1;
            grid[i][j] = 0;
            for(int[] dir: directions) {
                if(
                    (0<=(i+dir[0]))&&(i+dir[0]<grid.length)&&
                    (0<=(j+dir[1]))&&(j+dir[1]<grid[0].length)
                ) {
                    dfs(grid, i+dir[0], j+dir[1]);
                }
            }
        }
    }
}
