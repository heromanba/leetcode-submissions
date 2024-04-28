class Solution {
    public int countServers(int[][] grid) {
        int ret = 0;
        int[] rows = new int[grid.length];
        int[] cols = new int[grid[0].length];
        
        for(int i=0; i<grid.length; i++) {
            int tmp=0;
            for(int j=0; j<grid[0].length; j++) {
                if(grid[i][j]==1)
                    tmp++;
            }
            rows[i]=tmp;
        }
        for(int j=0; j<grid[0].length; j++) {
            int tmp=0;
            for(int i=0; i<grid.length; i++) {
                if(grid[i][j]==1)
                    tmp++;
            }
            cols[j]=tmp;
        }
        for(int i=0; i<grid.length; i++) {
            for(int j=0; j<grid[0].length; j++) {
                // System.out.println("i:"+i+"j:"+j+"rows:"+rows[i]+"cols:"+cols[j]);
                if((grid[i][j]==1)&&((rows[i]>1)||(cols[j]>1)))
                    ret++;
            }
        }
        return ret;
    }
}
