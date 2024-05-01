class Solution {
    private int[] parent = null;
    private int[] size = null;
    
    private int find(int i) {
        while(parent[i]!=i) {
            parent[i] = parent[parent[i]];
            i = parent[i];
        }
        return i;
    }
    
    private void union(int i, int j) {
        int iRoot = find(i);
        int jRoot = find(j);
        if(iRoot!=jRoot) {
            if(size[i]<size[j]) {
                parent[iRoot] = jRoot;
                size[jRoot] += size[iRoot];
            } else {
                parent[jRoot] = iRoot;
                size[iRoot] += size[jRoot];
            }
        }
    }
    
    private boolean isConnected(int i, int j) {
        return find(i)==find(j);
    }
    
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        parent = new int[n];
        size = new int[n];
        for(int i=0; i<n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
        for(int[] edge: edges) {
            union(edge[0], edge[1]);
        }
        return isConnected(source, destination);
    }
}
