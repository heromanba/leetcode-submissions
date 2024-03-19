class Solution {
    public void rotate(int[][] matrix) {
        float origin = (float) (1+matrix.length)/2;
        int target = matrix[0][0];
        int[][] ret = new int[matrix.length][matrix[0].length];
        for (int i=1; i<matrix.length+1; i++) {
            for (int j=1; j<matrix[0].length+1; j++) {
                int m = j;
                int n = (int)(2*origin-i);
                int tmp = matrix[m-1][n-1];
                ret[m-1][n-1] = matrix[i-1][j-1];
                // System.out.println("i"+i+"j"+j+"m"+m+"n"+n);
            }
        }
        for (int i=0; i<matrix.length; i++) {
            for (int j=0; j<matrix[0].length; j++) {
                matrix[i][j]=ret[i][j];
            }
        }
    }
}
