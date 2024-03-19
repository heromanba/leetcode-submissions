class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character,Integer> cnt=new HashMap<>();
        for(char c: magazine.toCharArray())
        {
            if(!cnt.containsKey(c))
                cnt.put(c,1);
            else
                cnt.put(c,cnt.get(c)+1);
        }
        for(char c: ransomNote.toCharArray())
        {
            if(!cnt.containsKey(c))
                return false;
            if(cnt.get(c)==0)
                return false;
            cnt.put(c,cnt.get(c)-1);
        }
        return true;
    }
}
