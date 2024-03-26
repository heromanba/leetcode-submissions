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
    public TreeNode replaceValueInTree(TreeNode root) {
        root.val = 0;
        List<TreeNode> currLevel = new ArrayList<>();
        currLevel.add(root);
        while (!currLevel.isEmpty()) {
            List<TreeNode> nextLevel = new ArrayList<>();
            int nextLevelSum = 0;
            for (int i=0; i<currLevel.size(); i++) {
                if (currLevel.get(i).left!=null) {
                    nextLevelSum += currLevel.get(i).left.val;
                }
                if (currLevel.get(i).right!=null) {
                    nextLevelSum += currLevel.get(i).right.val;
                }
                if (currLevel.get(i).left!=null) 
                    nextLevel.add(currLevel.get(i).left);
                if (currLevel.get(i).right!=null) 
                    nextLevel.add(currLevel.get(i).right);
            }
            for(int i=0;i<currLevel.size();i++) {
                int tmp = 0;
                if (currLevel.get(i).left!=null) {
                    tmp+=currLevel.get(i).left.val;
                }
                if (currLevel.get(i).right!=null) {
                    tmp+=currLevel.get(i).right.val;
                }
                if (currLevel.get(i).left!=null) {
                    currLevel.get(i).left.val=nextLevelSum-tmp;
                }
                if (currLevel.get(i).right!=null) {
                    currLevel.get(i).right.val=nextLevelSum-tmp;
                }
                
            }
            // System.out.println("tmp.size()"+tmp.size()+"currLevel.size()"+currLevel.size());
            currLevel = nextLevel;
        }
        return root;
    }
}
