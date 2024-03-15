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
    private int depMax = -1;
    private int val = 0;
    
    private void dfs(TreeNode node, int dep) {
        if (node==null)
            return;
        if ((node.left==null)&&(node.right==null)) {
            if (dep > depMax) {
                depMax=dep;
                val=node.val;
            }
            return;
        }
        dfs(node.left, dep+1);
        dfs(node.right, dep+1);       
    }

    public int findBottomLeftValue(TreeNode root) {
        
        dfs(root, 0);
        return val;
    }
}
