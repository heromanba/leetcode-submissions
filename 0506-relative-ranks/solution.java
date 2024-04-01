class Solution {
    public String[] findRelativeRanks(int[] score) {
        int[] old = new int[score.length];
        System.arraycopy(score, 0, old, 0, score.length);
        Arrays.sort(score);
        Map<Integer,String> tmp=new HashMap<>();
        for(int i=1;i<=score.length; i++){
            if(i==1){
                tmp.put(score[score.length-i],"Gold Medal");
            }else if(i==2){
                tmp.put(score[score.length-i],"Silver Medal");
            }else if(i==3){
                tmp.put(score[score.length-i],"Bronze Medal");
            }else
                tmp.put(score[score.length-i],String.valueOf(i));
        }
        String[] ret=new String[score.length];
        for(int i=0;i<score.length;i++){
            int n=old[i];
            ret[i]=tmp.get(n);
        }
        return ret;
    }
}
