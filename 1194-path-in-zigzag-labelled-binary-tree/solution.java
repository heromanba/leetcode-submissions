class Solution {
    public List<Integer> pathInZigZagTree(int label) {
        Deque<Integer> path = new LinkedList<>();
        while (label > 1) {
            path.addFirst(label);
            int level = (int)Math.floor(Math.log(label)/Math.log(2)+1);
            if (level % 2 == 0) {
                // even level, order is reversed
                int originalValue = (int)(Math.pow(2,level-1)+Math.pow(2, level)-1-label);
                int originalParent = (int)Math.floor(originalValue / 2);
                label = originalParent;
            } else {
                // odd level, order is correct
                int originalParent = (int)Math.floor(label / 2);
                int currentParent = (int)(Math.pow(2,level-2) + Math.pow(2,level-1)-1-originalParent);
                label = currentParent;
            }
        }
        path.addFirst(label);
        return (List)path;
    }
}
