class Solution {
    public Set<Integer> visited = new HashSet<>();
    public Set<Integer> inQueue = new HashSet<>();
    public Deque<int[][]> q = new LinkedList<>();

    public int matrixScore(int[][] grid) {
        for(int i=0; i<grid.length; i++) {
            if(grid[i][0]==0) {
                for(int j=0; j<grid[0].length; j++) {
                    grid[i][j] = 1 - grid[i][j];
                }
            }
        }
        for(int j=0; j<grid[0].length; j++) {
            int num0 = 0;
            for(int i=0; i<grid.length; i++) {
                if(grid[i][j]==0)
                    num0++;
            }
            if(num0>grid.length/2) {
                for(int i=0; i<grid.length; i++) {
                    grid[i][j] = 1 - grid[i][j];
                }
            }
        }
        return getBinSum(grid);
    }

    public int getBinSum(int[][] grid) {
        int sum = 0;
        for(int i=0; i<grid.length; i++) {
            for(int j=0; j<grid[0].length; j++) {
                // System.out.println("i: "+i+" j: "+j+" v: "+grid[i][j]);
                sum += grid[i][j] * Math.pow(2, grid[0].length-j-1);
            }
        }
        // System.out.println(sum);
        return sum;
    }
}
