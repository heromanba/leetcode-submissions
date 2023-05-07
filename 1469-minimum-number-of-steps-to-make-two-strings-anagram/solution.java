class Solution {
    public Map<Character, Integer> getCnt(String s) {
        Map<Character, Integer> cnt = new HashMap<>();
        for(int i=0; i<s.length(); i++) {
            Character c = s.charAt(i);
            if (!cnt.containsKey(c)) {
                cnt.put(c, 1);
            } else {
                cnt.put(c, cnt.get(c) + 1);
            }
        }
        return cnt;
    }
    public int minSteps(String s, String t) {
        Map<Character, Integer> sCnt = getCnt(s);
        Map<Character, Integer> tCnt = getCnt(t);
        int min = 0;
        for(Character k: sCnt.keySet()) {
            if (!tCnt.containsKey(k))
                min += sCnt.get(k);
            else {
                if (sCnt.get(k)>tCnt.get(k))
                    min += sCnt.get(k) - tCnt.get(k);
            }
        }
        return min;
    }
}
