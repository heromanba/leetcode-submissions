class Solution {
    public int[] xorQueries(int[] arr, int[][] queries) {
        int xor = 0;
        int[] mem = new int[arr.length];
        for(int i=0; i<arr.length; i++) {
            xor ^= arr[i];
            mem[i] = xor;
        }
        int[] ret = new int[queries.length];
        for(int i=0; i<queries.length; i++) {
            if(queries[i][0]==queries[i][1])
                ret[i] = arr[queries[i][0]];
            else if(queries[i][0]-1<0)
                ret[i] = mem[queries[i][1]];
            else
                ret[i] = mem[queries[i][0]-1] ^ mem[queries[i][1]];
        }
        return ret;
    }
}
