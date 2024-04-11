class Solution {
    public int maximumGroups(int[] grades) {
        int i=0;
        int tmp=0;
        while(true) {
            tmp+=i;
            if(tmp>grades.length)
                break;
            i++;
        }
        return i-1;
    }
}
