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
    public TreeNode pruneTree(TreeNode root) {
        return postOrder(root);
    }
    private TreeNode postOrder(TreeNode root) {
        if (root==null)
            return null;
        root.left = postOrder(root.left);
        root.right = postOrder(root.right);
        
        if((root.left==null)&&(root.right==null)) {
            if (root.val==0)
                return null;
        }
        return root;
    }
}
