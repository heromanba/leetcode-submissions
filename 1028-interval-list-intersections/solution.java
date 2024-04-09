class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        List<int[]> ret = new ArrayList<>();
        for(int i=0; i<firstList.length; i++) {
            for(int j=0; j<secondList.length; j++) {
                if(secondList[j][0]>firstList[i][1])
                    break;
                if(secondList[j][1]<firstList[i][0])
                    continue;
                int one = Math.max(firstList[i][0], secondList[j][0]);
                int two = Math.min(firstList[i][1], secondList[j][1]);
                int[] tmp = { one, two };
                ret.add( tmp );
            }
        }
            
        int[][] retArr = new int[ret.size()][2];
        for(int n=0; n<ret.size(); n++) {
            retArr[n] = ret.get(n);
        }
        return retArr;
    }
}
