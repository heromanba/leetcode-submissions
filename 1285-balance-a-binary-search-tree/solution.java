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
    public TreeNode balanceBST(TreeNode root) {
        List<Integer> visited = new ArrayList<>();
        Stack<TreeNode> toVisit = new Stack<>();
        
        TreeNode curr = root;
        while ((curr!=null)||(!toVisit.isEmpty())) {
            while (curr!=null){
                toVisit.push(curr);
                curr=curr.left;
            }
            curr=toVisit.pop();
            visited.add(curr.val);
            curr=curr.right;
        }
        return construct(visited, 0, visited.size());
    }
    
    private TreeNode construct(List<Integer> visited, int start, int end) {
        if (start==end) {
            return null;
        } 
        TreeNode root = new TreeNode(visited.get((start+end)/2));
        root.left = construct(visited, start, (start+end)/2);
        root.right = construct(visited, (start+end)/2+1, end);
        return root;
    }
    
}
