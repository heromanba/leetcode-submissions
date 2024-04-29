class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int src=image[sr][sc];
        if(src!=color)
            dfs(image, sr, sc, src, color);
        return image;
    }
    
    private void dfs(int[][] image, int i, int j, int src, int color){
        if(i<0||j<0||i>image.length-1||j>image[0].length-1)
            return;
        if(image[i][j]!=src)
            return;
        image[i][j]=color;
        dfs(image, i-1, j, src, color);
        dfs(image, i+1, j, src, color);
        dfs(image, i, j-1, src, color);
        dfs(image, i, j+1, src, color);
    }
}
