class Solution {
    public int equalPairs(int[][] grid) {
        int ret=0;
        for(int i=0;i<grid.length; i++)
        {
            for(int j=0;j<grid[0].length;j++)
            {
                if(isEqual(grid,i,j))
                    ret+=1;
            }
        }
        return ret;

    }
    private boolean isEqual(int[][] grid, int i, int j) {
        int[] row = grid[i];
        for (int k=0;k<grid.length;k++){
            if(row[k]!=grid[k][j])
                return false;
        }
        return true;
    }
}
