class Solution {
    public String smallestNumber(String pattern) {
        int lastI = -1;
        StringBuilder result = new StringBuilder();
        
        for (int i=0; i<pattern.length()+1; i++) {
            if ((i==pattern.length())||(pattern.charAt(i) == 'I')) {
                for (int j=i; j>lastI; j--) {
                    result.append(j+1);
                }
                lastI = i;
            }
        }
        return result.toString();
    }
}
