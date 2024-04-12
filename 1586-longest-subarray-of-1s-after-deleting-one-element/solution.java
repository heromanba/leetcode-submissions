class Solution {
    public int longestSubarray(int[] nums) {
        List<int[]> tmp=new ArrayList<>();
        int ones=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==0){
                if(!tmp.isEmpty())
                    tmp.get(tmp.size()-1)[1]=ones;
                int[] t=new int[2];
                t[0]=ones;
                tmp.add(t);
                ones=0;
            } else {
                
                ones++;
                if(i==nums.length-1){
                    if(!tmp.isEmpty())
                        tmp.get(tmp.size()-1)[1]=ones;
                }
            }
        }
        if(tmp.isEmpty())
            return nums.length-1;
        else{
            int max=-1;
            for(int[] t:tmp) {
                int n=t[0]+t[1];
                if(n>max)
                    max=n;
            }
            return max;
        }

    }
}
