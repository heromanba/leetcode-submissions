class Solution {
    public String removeOccurrences(String s, String part) {
        for (int i=0; i<s.length()-part.length()+1; i++) {
            if (s.substring(i, i+part.length()).equals(part)) {
                String newS = s.substring(0, i) + s.substring(i+part.length());
                return removeOccurrences(newS, part);
            }
        }
        return s;
    }
}
