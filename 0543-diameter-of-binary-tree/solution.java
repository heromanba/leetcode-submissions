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
    private int ret = -1;
    
    public int diameterOfBinaryTree(TreeNode root) {
        postorder(root);
        return ret;
    }
    
    private int postorder(TreeNode root) {
        if (root==null)
            return 0;
        int left= postorder(root.left);
        int right= postorder(root.right);
        int diameter = left+right;
        if(diameter>ret)
            ret=diameter;
        return Math.max(left, right)+1;
        
    }
}
