class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> cnt = new HashMap<>();
        Set<Character> dup=new HashSet<>();
        for(int i=0; i<s.length(); i++) {
            if(cnt.containsKey(s.charAt(i))) {
                dup.add(s.charAt(i));
            }
            else
                cnt.put(s.charAt(i), i);
        }
        int min = s.length();
        for(Map.Entry<Character, Integer> entry: cnt.entrySet()) {
            if((entry.getValue()<min)&&(!dup.contains(entry.getKey())))
                min=entry.getValue();
        }
        if(min==s.length())
            return -1;
        else
            return min;
    }
}
