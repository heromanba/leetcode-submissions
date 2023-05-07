class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        Arrays.sort(deck);
        if (deck.length < 3)
            return deck;
        Deque<Integer> ret = new ArrayDeque<>();
        ret.addLast(deck[deck.length-2]);
        ret.addLast(deck[deck.length-1]);
        for(int i=3; i<deck.length+1; i++) {
            ret.addFirst(ret.removeLast());
            ret.addFirst(deck[deck.length-i]);
        }
        int[] result = new int[ret.size()];
        int i=0;
        while (!ret.isEmpty()) {
            result[i] = ret.removeFirst();
            i++;
        }
        return result;
    }
}
