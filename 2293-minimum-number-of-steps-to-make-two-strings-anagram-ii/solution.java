class Solution {
    public int minSteps(String s, String t) {
        int[] sChar = new int[26];
        int[] tChar = new int[26];
        for (Character c: s.toCharArray()) {
            sChar[(int)c-'a'] += 1;
        }
        for (Character c: t.toCharArray()) {
            tChar[(int)c-'a'] += 1;
        }
        int cnt = 0;
        for (int i=0; i<26; i++)
            cnt += Math.abs(sChar[i]-tChar[i]);
        return cnt;
    }
}
