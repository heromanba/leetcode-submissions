class Solution {
    public int maximumBags(int[] capacity, int[] rocks, int additionalRocks) {
        int tmp=0;
        for(int i=0;i<capacity.length;i++){
            capacity[i]-=rocks[i];
        }
        Arrays.sort(capacity);
        for(int i=0;i<capacity.length;i++){
            if(capacity[i]<=additionalRocks) {
                additionalRocks-=capacity[i];
                tmp++;
            } else
                break;
        }
        return tmp;
    }
}
