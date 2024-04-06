class Solution {
    public List<List<Integer>> queensAttacktheKing(int[][] queens, int[] king) {
        int[][] directions = {
            {0,-1},
            {-1,-1},
            {-1,0},
            {-1,1},
            {0,1},
            {1,1},
            {1,0},
            {1,-1}
        };
        List<List<Integer>> ret = new ArrayList<>();
        
        for(int[] dir: directions) {
            int x=king[0];
            int y=king[1];
            while(
                (0<=x)&&(x<=8)&&
                (0<=y)&&(y<=8)
            ) {
                x+=dir[0];
                y+=dir[1];
                boolean found = false;
                for(int[] queen: queens) {
                    if((queen[0]==x)&&(queen[1]==y)) {
                        List<Integer> tmp = new ArrayList<>();
                        tmp.add(queen[0]);
                        tmp.add(queen[1]);
                        ret.add(tmp);
                        found = true;
                        break;
                    }
                }
                if(found)
                    break;
            }
        }
        return ret;
    }
}
