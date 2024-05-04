class Solution {
    public int[] findDiagonalOrder(List<List<Integer>> nums) {
        int size = 0;
        List<List<Integer>> ret = new ArrayList<>();
        for(int i=0; i<nums.size(); i++) {
            for(int j=0; j<nums.get(i).size(); j++) {
                if(i+j>=ret.size()) {
                    List<Integer> tmp = new ArrayList<>();
                    tmp.add(nums.get(i).get(j));
                    ret.add(tmp);
                } else {
                    List<Integer> tmp = ret.get(i+j);
                    tmp.add(nums.get(i).get(j));
                }
                size++;
            }
        }
        int[] retArray = new int[size];
        int cnt = 0;
        for(List<Integer> tmp: ret) {
            for(int i=tmp.size()-1; i>=0; i--) {
                retArray[cnt] = tmp.get(i);
                cnt++;
            }
        }
        return retArray;
    }
}
