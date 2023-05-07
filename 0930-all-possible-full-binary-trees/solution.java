/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public Map<Integer, List<TreeNode>> mem = new HashMap<>();

    public TreeNode clone(TreeNode node) {
        if (node == null)
            return null;
        TreeNode newLeft = clone(node.left);
        TreeNode newRight = clone(node.right);
        TreeNode newNode = new TreeNode(node.val, newLeft, newRight);
        return newNode;
    }
    public List<TreeNode> allPossibleFBT(int n) {
        if (n == 1)
            return List.of(new TreeNode());
        if (mem.containsKey(n))
            return mem.get(n);
        else {
            List<TreeNode> ret = new ArrayList<>();
            for(int i=1; i<n; i+=2) {
                List<TreeNode> possibleLeft = allPossibleFBT(i);
                List<TreeNode> possibleRight = allPossibleFBT(n-1-i);
                for(TreeNode left:possibleLeft) {
                    for (TreeNode right:possibleRight) {
                        ret.add( new TreeNode(0, left, right) );
                    }
                }
            }
            mem.put(n, ret);
            return ret;
        }
    }
}
