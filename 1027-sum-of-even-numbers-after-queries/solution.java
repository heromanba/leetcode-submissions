class Solution {
    public int[] sumEvenAfterQueries(int[] nums, int[][] queries) {
        int tmp=0;
        for(int i:nums){
            if(i%2==0)
                tmp+=i;
        }
        int[] ret=new int[queries.length];
        for(int i=0;i<queries.length;i++) {
            int[] q=queries[i];
            int old=nums[q[1]];
            if(old%2==0)
                tmp-=old;
            int new1=old+q[0];
            nums[q[1]]=new1;
            if(new1%2==0)
                tmp+=new1;
            ret[i]=tmp;
        }
        return ret;
    }
}
