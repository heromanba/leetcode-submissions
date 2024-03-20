class Solution {
    public char findTheDifference(String s, String t) {
        Map<Character,Integer> cnt=new HashMap<>();
        for(Character c:s.toCharArray()){
            if(!cnt.containsKey(c))
                cnt.put(c,1);
            else
                cnt.put(c,cnt.get(c)+1);
        }
        for(Character c:t.toCharArray()){
            if(!cnt.containsKey(c)||(cnt.get(c)==0))
                return c;
            cnt.put(c,cnt.get(c)-1);
        }
        return 0;
    }
}
