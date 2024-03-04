class Solution {
    public int[][] matrixBlockSum(int[][] mat, int k) {
        int[][] ret = new int[mat.length][mat[0].length];
        for (int i=0; i<mat.length; i++) {
            for (int j=0; j<mat[0].length; j++) {
                int temp = 0;
                for (int r=i-k; r<= i+k; r++) {
                    for (int c=j-k; c<=j+k; c++) {
                        if ((0<=r)&&(r<mat.length)&&(0<=c)&&(c<mat[0].length)) {
                            temp+=mat[r][c];
                        }
                    }
                }
                ret[i][j] = temp;
            }
        }
        return ret;
    }
}
