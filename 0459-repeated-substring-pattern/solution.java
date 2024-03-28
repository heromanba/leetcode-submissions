class Solution {
    public boolean repeatedSubstringPattern(String s) {
        boolean ret = false;
        for(int i=1 ; i<s.length(); i++) {
            if(s.length()%i==0) {
                boolean notEqual = false;
                for(int j=0; j<s.length()/i; j++) {
                    // System.out.println("i"+i+"j"+j+"s.length()/i"+s.length()/i);
                    // System.out.println(s.substring(0, i)+" "+s.substring(i*j,i*(j+1)));
                    if(!s.substring(0, i).equals(s.substring(i*j,i*(j+1)))) {
                        notEqual=true;
                        break;
                    }
                }
                if(!notEqual)
                    return true;
            }
        }
        return ret;
    }
}
