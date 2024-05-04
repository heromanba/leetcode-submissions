class Solution {
    public String largestWordCount(String[] messages, String[] senders) {
        String ret = null;
        int max = -1;
        
        Map<String, Integer> counter = new HashMap<>();
        for(int i=0; i<messages.length; i++) {
            int tmp = 1;
            String s = messages[i];
            for(int j=0; j<s.length(); j++) {
                if(s.charAt(j)==' ')
                    tmp++;
            }
            String ss = senders[i];
            if(counter.containsKey(ss))
                counter.put(ss, counter.get(ss)+tmp);
            else
                counter.put(ss, tmp);
        }
        
        for(Map.Entry<String, Integer> entry: counter.entrySet()) {
            int tmp = entry.getValue();
            if(
                (tmp>max)||
                (
                    (tmp==max)&&
                    (entry.getKey().compareTo(ret)>0))
                ) {
                max = tmp;
                ret = entry.getKey();
            }
        }
        return ret;
    }
}
