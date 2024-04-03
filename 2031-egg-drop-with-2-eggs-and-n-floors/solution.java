class Solution {
    public int twoEggDrop(int n) {
        int i=1;
        while(true){
            if(n>i){
                n-=i;
                i+=1;
            }else{
                break;
            }
        }
        return i;
    }
}
