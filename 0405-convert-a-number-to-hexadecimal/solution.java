class Solution {
    public String toHex(int num) {
        if(num==0)
            return "0";
        if(num>0){
            StringBuilder sb=new StringBuilder();
            while(num>0){
                if(num%16>9)
                    sb.append((char)('a'+num%16-10));
                else
                    sb.append(num%16);
                num/=16;
            }
            return sb.reverse().toString();
        } else {
            StringBuilder sb=new StringBuilder();
            long num2=(long)(Math.pow(2,32)-1)+num;
            //System.out.println(num2);
            num2+=1;
            //System.out.println(num2);
            while(num2>0){
                if(num2%16>9)
                    sb.append((char)('a'+num2%16-10));
                else
                    sb.append(num2%16);
                num2/=16;
            }
            return sb.reverse().toString();
        }
    }
}
