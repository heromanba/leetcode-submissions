class Solution {
    public int findJudge(int n, int[][] trust) {
        int[] inDegree = new int[n];
        int[] outDegree = new int[n];
        for(int[] tmp: trust) {
            outDegree[tmp[0]-1] += 1;
            inDegree[tmp[1]-1] += 1;
        }
        int ret = -1;
        for(int i=0; i<n; i++) {
            if((inDegree[i]==n-1)&&(outDegree[i]==0))
                return i+1;
        }
        return ret;
    }
}
