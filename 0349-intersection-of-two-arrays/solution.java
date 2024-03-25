class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> s1=new HashSet<Integer>();
        for(int i:nums1)
            s1.add(i);
        Set<Integer> s2=new HashSet<Integer>();
        for(int i:nums2)
            s2.add(i);
        Set<Integer> s3=new HashSet<>();
        s1.retainAll(s2);
        int[] ret=new int[s1.size()];
        int n=0;
        for(int i:s1){
            ret[n]=i;
            n+=1;
        }
        return ret;
    }
}
