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
    public int numGood = 0;
    public void preOrder(TreeNode node, int max) {
        if(node == null)
            return;
        if(node.val >= max) {
            max = node.val;
            numGood++;
        }
        if(node.left != null)
            preOrder(node.left, Math.max(node.left.val, max));
        if(node.right != null)
            preOrder(node.right, Math.max(node.right.val, max));
    }
    public int goodNodes(TreeNode root) {
        preOrder(root, Integer.MIN_VALUE);
        return numGood;
    }
}
