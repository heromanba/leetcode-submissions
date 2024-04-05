class Solution {
    public int findComplement(int num) {
        int pow=(int)(Math.log(num)/Math.log(2)+1);
        int tmp=(int)(Math.pow(2,pow)-1);
        //System.out.println("pow"+pow+"tmp"+tmp);
        return num^tmp;
    }
}
