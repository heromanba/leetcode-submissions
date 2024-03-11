class Solution {
    public boolean isIsomorphic(String s, String t) {
        Map<Character, Character> stmap = new HashMap<>();
        Map<Character, Character> tsmap = new HashMap<>();
        for (int i=0; i<s.length(); i++) {
            if ((!stmap.containsKey(s.charAt(i)))&&(!tsmap.containsKey(t.charAt(i)))) {
                stmap.put(s.charAt(i), t.charAt(i));
                tsmap.put(t.charAt(i), s.charAt(i));
            }               
            else {
                if (stmap.containsKey(s.charAt(i))&&(stmap.get(s.charAt(i))!=t.charAt(i)))
                    return false;
                if (tsmap.containsKey(t.charAt(i))&&(tsmap.get(t.charAt(i))!=s.charAt(i)))
                    return false;
            }
        }
        return true;
    }
}
