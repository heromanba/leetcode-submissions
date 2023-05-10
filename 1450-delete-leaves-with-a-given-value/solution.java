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
    public void postOrder(TreeNode node, TreeNode parent, int target) {
        if (node == null)
            return;
        postOrder(node.left, node, target);
        postOrder(node.right, node, target);
        if ((node.left == null) && (node.right == null) && (node.val == target)) {
            System.out.println(node.val);
            if(parent.left == node) {
                parent.left = null;
            } else {
                parent.right = null;
            }
            return;
        }
    }
    public TreeNode removeLeafNodes(TreeNode root, int target) {
        TreeNode sentinel = new TreeNode(0, root, null);
        postOrder(sentinel.left, sentinel, target);
        return sentinel.left;
    }
}
