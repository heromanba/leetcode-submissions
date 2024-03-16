class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> ret = new ArrayList<>();
        if (nums.length==0)
            return ret;
        if (nums.length==1){
            ret.add(String.valueOf(nums[0]));
            return ret;
        }
        int start=nums[0];
        int end=start;
        for(int i=0;i<nums.length;i++) {
            //System.out.println("i"+i+"start"+start+"end"+end);
            if((i==nums.length-1)||(nums[i+1]>end+1)){
                if(start!=end)
                    ret.add(start+"->"+end);
                else
                    ret.add(String.valueOf(start));
                if (i!=nums.length-1)
                    start=nums[i+1];
                end=start;
            } else
                end=nums[i+1];
        }
        return ret;
    }
}
