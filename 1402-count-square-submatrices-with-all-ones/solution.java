class Solution {
    public int countSquares(int[][] matrix) {
        int maxSquareSize = matrix.length;
        if (matrix.length>matrix[0].length)
            maxSquareSize = matrix[0].length;
        int ret = 0;
        
        int[][] tmp = matrix;
        for (int i=0; i<tmp.length; i++) {
            for (int j=0; j<tmp[0].length; j++) {
                if (tmp[i][j]==1) {
                    ret += 1;
                }
            }
        }
        
        for (int size=2; size<=maxSquareSize; size++) {
            int[][] tmp2 = new int[tmp.length-1][tmp[0].length-1];
            for (int i=0; i<tmp.length-1; i++) {
                for (int j=0; j<tmp[0].length-1; j++) {
                    if (isSquare(tmp, i, j, 2)==1) {
                        tmp2[i][j]=1;
                        ret += 1;
                    }
                }
            }
            tmp=tmp2;
            
        }
        return ret;
    }
    
    public int isSquare(int[][] matrix, int i, int j, int n) {
        for (int row=i; row<i+n; row++) {
            for (int col=j; col<j+n; col++) {
                if (matrix[row][col] != 1)
                    return 0;
            }
        }
        return 1;
    }
}
