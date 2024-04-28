class Solution {
    private int[] id = null;
    private int[] size = null;
    private int count = 0;
    
    private int find(int i) {
        while(id[i]!=i) {
            id[i]=id[id[i]];
            i=id[i];
        }
        return i;
    }
    
    private void union(int i, int j) {
        int iRoot = find(i);
        int jRoot = find(j);
        if(iRoot!=jRoot) {
            if(size[i]>size[j]) {
                id[jRoot]=iRoot;
                size[i]+=size[j];
            } else {
                id[iRoot]=jRoot;
                size[j]+=size[i];
            }
            count--;
        }
    }
    public int findCircleNum(int[][] isConnected) {
        id = new int[isConnected.length];
        size = new int[isConnected.length];
        for(int i=0; i<isConnected.length; i++) {
            id[i]=i;
            size[i]=1;
        }
        count = isConnected.length;
        
        for(int i=0; i<isConnected.length; i++) {
            for(int j=i+1; j<isConnected[0].length; j++) {
                if(isConnected[i][j]==1) {
                    union(i, j);
                }
            }
        }
        return count;
    }
    
}
