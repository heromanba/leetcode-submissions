class Solution {
    private int[] id = null;
    private int[] size = null;
    private int count = 0;
    
    private int find(int i) {
        while(id[i]!=i) {
            id[i]=id[id[i]];
            i = id[i];
        }
        return i;
    }
    private boolean union(int i, int j) {
        int iRoot = find(i);
        int jRoot = find(j);
        boolean alreadyConnected = true;
        if(iRoot!=jRoot) {
            if(size[iRoot]>size[jRoot]) {
                id[jRoot] = iRoot;
                size[iRoot]+=size[jRoot];
            } else {
                id[iRoot] = jRoot;
                size[jRoot]+=size[iRoot];
            }
            alreadyConnected=false;
            count--;
        }
        return alreadyConnected;
    }
    public int makeConnected(int n, int[][] connections) {
        id = new int[n];
        size = new int[n];
        for(int i=0; i<n; i++) {
            id[i]=i;
            size[i]=1;
        }
        count = n;
        int canUse = 0;
        for(int[] con: connections) {
            boolean alreadyConnected = union(con[0], con[1]);
            if(alreadyConnected)
                canUse++;
        }
        // System.out.println("canUse:"+canUse+"count:"+count);
        if(canUse>=count-1)
            return count-1;
        else
            return -1;
    }
}
