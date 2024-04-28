class Solution {
    int[] id = null;
    int[] size = null;
    
    private int find(int i) {
        while(id[i]!=i) {
            id[i] = id[id[i]];
            i = id[i];
        }
        return i;
    }
    
    private boolean union(int i, int j) {
        int iRoot = find(i);
        int jRoot = find(j);
        
        boolean alreadyConnected = true;
        if(iRoot!=jRoot) {
            if(size[iRoot]<size[jRoot]) {
                id[jRoot] = id[iRoot];
                size[iRoot]+=size[jRoot];
            } else {
                id[iRoot] = id[jRoot];
                size[jRoot] += size[iRoot];
            }
            alreadyConnected = false;
        }
        return alreadyConnected;
    }
    
    public int[] findRedundantConnection(int[][] edges) {
        int n = 0;
        for(int[] edge: edges) {
            if(edge[0]>n)
                n=edge[0];
            if(edge[1]>n)
                n=edge[1];
        }
        id = new int[n];
        size = new int[n];
        for(int i=0; i<n; i++) {
            id[i]=i;
            size[i]=1;
        }
        int[] ret = null;
        for(int[] edge: edges) {
            boolean alreadyConnected = union(edge[0]-1, edge[1]-1);
            if(alreadyConnected)
                ret = edge;
        }
        return ret;
    }
}
