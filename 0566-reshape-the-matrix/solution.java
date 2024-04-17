class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        if(r*c!=mat.length*mat[0].length)
            return mat;
        int[][] ret = new int[r][c];
        int cnt = 0;
        for(int i=0; i<mat.length; i++) {
            for(int j=0; j<mat[0].length; j++) {
                int m = cnt / c;
                int n = cnt % c;
                ret[m][n] = mat[i][j];
                cnt++;
                // System.out.println("cnt:"+cnt+"m:"+m+"n:"+n);
            }
        }
        return ret;
    }
}
