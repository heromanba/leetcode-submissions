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
    private int ret = 0;
    private int postOrder(TreeNode node) {
        if (node==null)
            return 0;
        int fromLeft = postOrder(node.left);
        int fromRight = postOrder(node.right);
        int steps = fromLeft+fromRight+node.val-1;
        ret += Math.abs(steps);
        return steps;
    }
    public int distributeCoins(TreeNode root) {
        postOrder(root);
        return ret;
    }
}
