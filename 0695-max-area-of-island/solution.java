class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int cc=0;
        Set<Map.Entry<Integer, Integer>> conflicts = new HashSet<>();
        for(int i=0; i<grid.length; i++) {
            for(int j=0; j<grid[0].length; j++) {
                if(grid[i][j]==1) {
                    if(
                        (i-1>=0)&&(grid[i-1][j]!=0)&&
                        (j-1>=0)&&(grid[i][j-1]!=0)&&
                        (grid[i-1][j]!=grid[i][j-1])
                    ) {
                        int smaller = Math.min(grid[i-1][j], grid[i][j-1]);
                        int bigger = Math.max(grid[i-1][j], grid[i][j-1]);
                        // System.out.println("i"+i+"j"+j+"b:"+bigger+"s:"+smaller);
                        conflicts.add(Map.entry(bigger, smaller));
                        grid[i][j] = smaller;
                    }
                    else if((i-1>=0)&&(grid[i-1][j]!=0)) {
                        grid[i][j] = grid[i-1][j];
                    }
                    else if((j-1)>=0&&(grid[i][j-1]!=0)) {
                        grid[i][j] = grid[i][j-1];
                    } else {
                        cc++;
                        grid[i][j] = cc;
                    }
                }
            }
        }
        // System.out.println(Arrays.deepToString(grid));
        
        int[] arr = new int[cc];
        for(int i=0; i<cc; i++)
            arr[i]=i+1;
        
        for(Map.Entry<Integer, Integer> entry: conflicts) {
            int p = root(arr, entry.getKey());
            int q = root(arr, entry.getValue());
            arr[p-1] = q;
        }
        
        for(int i=0; i<grid.length; i++) {
            for(int j=0; j<grid[0].length; j++) {
                if(grid[i][j]!=0) {
                    int root = root(arr, grid[i][j]);
                    grid[i][j] = root;
                }
            }
        }

        Map<Integer, Integer> cnt = new HashMap<>();
        
        for(int i=1; i<=cc; i++) {
            cnt.put(i, 0);
        }
        
        for(int i=0; i<grid.length; i++) {
            for(int j=0; j<grid[0].length; j++) {
                if(grid[i][j]!=0) {
                    cnt.put(grid[i][j], cnt.get(grid[i][j])+1);
                }
            }
        }
        
        // System.out.println(Arrays.toString(arr));
        // System.out.println(cnt);
        
        int maxArea = 0;
        for(Map.Entry<Integer, Integer> tmp: cnt.entrySet()) {
            if (tmp.getValue() > maxArea)
                maxArea = tmp.getValue();
        } 
        return maxArea;
    }
    
    private int root(int[] arr, int root) {
        while(arr[root-1]!=root)
            root = arr[root-1];
        return root;
    }
}
