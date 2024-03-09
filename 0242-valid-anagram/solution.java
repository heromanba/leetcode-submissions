class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> sCnt = new HashMap<>();
        Map<Character, Integer> tCnt = new HashMap<>();
        for (char c: s.toCharArray()) {
            if (sCnt.containsKey(c))
                sCnt.put(c, sCnt.get(c)+1);
            else
                sCnt.put(c, 1);
        }
        for (char c: t.toCharArray()) {
            if (tCnt.containsKey(c))
                tCnt.put(c, tCnt.get(c)+1);
            else
                tCnt.put(c, 1);
        }
        return sCnt.equals(tCnt);
    }
}
