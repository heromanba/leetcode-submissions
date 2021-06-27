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
    public TreeNode recoverFromPreorder(String traversal) {
        // the elements in the stack should be the path from the leaf to the root
        Stack<TreeNode> stack = new Stack<>();
        for (int i = 0; i < traversal.length();) {
            // Get node level;
            int level = 0;
            while(i < traversal.length() && traversal.charAt(i) == '-') {
                level++;
                i++;
            }
            
            // Get node value;
            int start = i;
            while(i < traversal.length() && Character.isDigit(traversal.charAt(i))) {
                i++;
            }
            int val = Integer.parseInt(traversal.substring(start, i));
            
            // Node to put in the tree;
            TreeNode tmp = new TreeNode(val);
            if (stack.isEmpty()) {
                // case 1: tmp is root node;
                stack.push(tmp);
            } else {
                // Get the level of the node at the top of the stack;
                // **stack.size() - 1 is the level**;
                // As long as stack.size() == level of tmp node, then
                // the top node is the parent of tmp node. Otherwise, 
                // keep popping.
                while(stack.size() > level)
                    stack.pop();
                if(stack.peek().left == null)
                    stack.peek().left = tmp;
                else
                    stack.peek().right = tmp;               
                stack.push(tmp);
            }
            System.out.println("value: " + val + "level:" + level);
        }
        while(stack.size() > 1)
            stack.pop();
        return stack.peek();
    }
}
