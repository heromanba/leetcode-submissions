class Solution {
    public String findDifferentBinaryString(String[] nums) {
        Arrays.sort(nums);
        int maxLen = (int) Math.pow(2, nums[0].length());
        for (int i=0; i<maxLen; i++) {
            if (i > nums.length-1)
                return binaryRepr(i, nums[0].length());
            String s = nums[i];
            int num = 0;
            for (int j=s.length()-1; j>=0; j--) {
                if (s.charAt(j)=='1') {
                    num += Math.pow(2, s.length()-1-j);
                }
            }
            // System.out.println("num: "+num+" i: "+i);
            if (num != i)
                return binaryRepr(i, nums[0].length());
        }
        return "";
    }
    
    private String binaryRepr(int i, int sLen) {
        StringBuilder ret = new StringBuilder();
        while (i != 0) {
            ret.append(i%2);
            i /= 2;
        }
        int numZeroToAppend = sLen - ret.length();
        for (int j=0; j<numZeroToAppend; j++)
            ret.append("0");
        return ret.reverse().toString();
    }
}
