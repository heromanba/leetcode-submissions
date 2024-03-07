class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
        Map<Integer, Integer> loserMap = new HashMap<>();
        Set<Integer> winners = new HashSet<>();
        for (int[] match: matches) {
            if (loserMap.containsKey(match[1])) {
                loserMap.put(match[1], loserMap.get(match[1])+1);
            } else {
                loserMap.put(match[1], 1);
                winners.remove(match[1]);
            }
            if (!loserMap.containsKey(match[0])) {
                winners.add(match[0]);
            }
        }
        List<Integer> lostOneMatch = new ArrayList<>();
        for (Map.Entry<Integer, Integer> loserEntry: loserMap.entrySet()) {
            if (loserEntry.getValue()==1)
                lostOneMatch.add(loserEntry.getKey());
        }
        List<Integer> lostNoMatch = new ArrayList<>();
        lostNoMatch.addAll(winners);
        List<List<Integer>> ret = new ArrayList<>();
        Collections.sort(lostNoMatch);
        Collections.sort(lostOneMatch);
        ret.add(lostNoMatch);
        ret.add(lostOneMatch);
        return ret;
    }
}
