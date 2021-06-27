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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        List<Integer> preorderList = Arrays.stream(preorder).boxed().collect(Collectors.toList());
        List<Integer> inorderList = Arrays.stream(inorder).boxed().collect(Collectors.toList());

        return buildTreeHelper(preorderList, inorderList);
    }
    
    public TreeNode buildTreeHelper(List<Integer> preorderList, List<Integer> inorderList) {
        
        // Base case
        if (preorderList.size() == 0)
            return null;
        
        if (preorderList.size() == 1)
            return new TreeNode(preorderList.get(0));
        
        // Get node value of root, left, right;
        int rootVal = preorderList.get(0);
        int leftChildVal = preorderList.get(1);
        
        // Find root node in inorder traversal;
        TreeNode root = new TreeNode(rootVal);
        int rootIdxInorder = inorderList.indexOf(rootVal);
        
        // No left subtree
        if (rootIdxInorder == 0) {
            root.left = null;
            root.right = buildTreeHelper(
                preorderList.subList(1, preorderList.size()), 
                inorderList.subList(1, inorderList.size())
            );
            return root;
        }
        
        // No right subtree
        if (rootIdxInorder == inorderList.size() - 1) {
            root.right = null;
            root.left = buildTreeHelper(
                preorderList.subList(1, preorderList.size()),
                inorderList.subList(0, inorderList.size() - 1)
            );
            return root;
        }
        
        // Find left subtree in inorder traversal
        int leftTreeSize = rootIdxInorder;
        
        List<Integer> leftSubTreeInorderList = inorderList.subList(0, rootIdxInorder);
        List<Integer> leftSubTreePreorderList = preorderList.subList(1, leftTreeSize + 1);
        
        List<Integer> rightSubTreeInorderList = inorderList.subList(rootIdxInorder + 1, inorderList.size());
        List<Integer> rightSubTreePreorderList = preorderList.subList(leftTreeSize + 1, preorderList.size());
        
        root.left = buildTreeHelper(leftSubTreePreorderList, leftSubTreeInorderList);
        root.right = buildTreeHelper(rightSubTreePreorderList, rightSubTreeInorderList);    
                            
        return root;
    }
}
