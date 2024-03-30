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
    private List<Integer> ret = new ArrayList<>();
    private Integer prev = null;
    private Integer freq = 0;
    private Integer maxFreq = -1;
    
    private void inorder(TreeNode root) {
        if(root==null)
            return;
        inorder(root.left);
        
        if((prev!=null)&&(root.val==prev)) {
            freq += 1;
        } else {
            freq = 1;
        }
        if(freq==maxFreq) {
            ret.add(root.val);
        }
        else if(freq>maxFreq) {
            ret = new ArrayList<>();
            ret.add(root.val);
            maxFreq = freq;
        }
        prev = root.val;
        
        inorder(root.right);
    }
    public int[] findMode(TreeNode root) {
        inorder(root);
        int[] retArr = new int[ret.size()];
        for(int i=0; i<ret.size(); i++) {
            retArr[i]=ret.get(i);
        }
        return retArr;
    }
}
