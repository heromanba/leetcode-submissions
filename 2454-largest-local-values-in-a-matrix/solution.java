class Solution {
    public int[][] largestLocal(int[][] grid) {
        int[][] ret = new int[grid.length-2][grid[0].length-2];
        for(int i=1; i<grid.length-1; i++) {
            for(int j=1; j<grid[0].length-1; j++) {
                int max = -1;
                for(int m=i-1; m<=i+1; m++) {
                    for(int n=j-1; n<=j+1; n++) {
                        if(grid[m][n]>max)
                            max=grid[m][n];
                    }
                }
                ret[i-1][j-1] = max;
            }
        }
        return ret;
    }
}
