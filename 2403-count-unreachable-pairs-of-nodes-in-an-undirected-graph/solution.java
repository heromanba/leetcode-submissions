class Solution {
    int[] parent = null;
    int[] size = null;
    
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
            if(size[iRoot]>size[jRoot]) {
                parent[jRoot]=iRoot;
                size[iRoot]+=size[jRoot];
            } else {
                parent[iRoot]=jRoot;
                size[jRoot]+=size[iRoot];
            }
        }
    }
    public long countPairs(int n, int[][] edges) {
        parent = new int[n];
        size = new int[n];
        for(int i=0; i<n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
        for(int[] edge: edges) {
            union(edge[0], edge[1]);
        }
        long ans = 0;
        long sum = 0;
        for(int i=0; i<n; i++){
            if(parent[i]==i){
                ans = ans + sum*size[i];
                sum = sum + size[i];
            }
        }
        return ans;
    }
}
