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
    private int maxDep=-1;
    private TreeNode subtree=null;
    
    private List<TreeNode> deepNodes=new ArrayList<>();
    
    public TreeNode subtreeWithAllDeepest(TreeNode root) {
        preOrder(root, 0);
        lca(root);
        return subtree;
    }
    
    private int lca(TreeNode root){
        if (root==null)
            return 0;
        int l=lca(root.left);
        int r=lca(root.right);
        int idx=deepNodes.indexOf(root);
        int ret=l|r;
        if(idx!=-1) {
            ret=ret|(int)(Math.pow(2,idx));
        } 
        if((subtree==null)&&(ret==(int)Math.pow(2,deepNodes.size())-1)){
            subtree=root;
        }
        return ret;
            
    }
    private void preOrder(TreeNode root, int depth) {
        if(root==null)
            return;
        if ((root.left==null)&&(root.right==null)) {
            if(depth>maxDep){
                maxDep=depth;
                deepNodes=new ArrayList<>();
                deepNodes.add(root);
            } else if (depth==maxDep) {
                deepNodes.add(root);
            }
            return;
        }
        preOrder(root.left, depth+1);
        preOrder(root.right, depth+1);
    }
}
