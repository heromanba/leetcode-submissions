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
    public int kthSmallest(TreeNode root, int k) {
        int cnt=0;
        Stack<TreeNode> s=new Stack<>();
        TreeNode curr=root;
        s.push(root);
        while(!s.isEmpty()){
            while(curr!=null){
                s.push(curr);
                curr=curr.left;
            }
            curr=s.pop();
            cnt+=1;
            if(cnt==k)
                return curr.val;
            curr=curr.right;
            
        }
        return 0;
        
    }
}
