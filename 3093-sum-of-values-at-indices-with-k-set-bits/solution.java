class Solution {
    public int sumIndicesWithKSetBits(List<Integer> nums, int k) {
        int ret = 0;
        for(int i=0; i<nums.size(); i++) {
            int j = i;
            int tmp=0;
            while(j!=0) {
                if(j%2==1)
                    tmp++;
                if(tmp>k)
                    break;
                j=j>>1;
                // System.out.println(j);
            }
            if(tmp==k)
                ret+=nums.get(i);
        }
        return ret;
    }
}
