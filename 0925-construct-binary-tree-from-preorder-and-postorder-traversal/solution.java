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
    public TreeNode constructFromPrePost(int[] preorder, int[] postorder) {
        //return null;
        return construct(preorder, postorder);
    }
    
    private TreeNode construct(int[] preorder, int[] postorder) {
        if(preorder.length==0)
            return null;
        if(preorder.length==1)
            return new TreeNode(preorder[0]);
        if(preorder.length==2) {
            TreeNode root = new TreeNode(preorder[0]);
            TreeNode left = new TreeNode(preorder[1]);
            root.left = left;
            return root;
        }
        
        TreeNode root = new TreeNode(preorder[0]);
        
        int leftPostIdx = indexOf(postorder, preorder[1]);
        int rightPreIdx = preorder.length;
        if(preorder[1]!=postorder[postorder.length-2])
            rightPreIdx=indexOf(preorder, postorder[postorder.length-2]);
        
        int[] leftPreorder = Arrays.copyOfRange(preorder, 1, rightPreIdx);
        int[] leftPostorder = Arrays.copyOfRange(postorder, 0, leftPostIdx+1);
        root.left = construct(leftPreorder, leftPostorder);
        
        int[] rightPreorder = Arrays.copyOfRange(preorder, rightPreIdx, preorder.length);
        int[] rightPostorder = Arrays.copyOfRange(postorder, leftPostIdx+1, preorder.length-1);
        root.right = construct(rightPreorder, rightPostorder);
        return root;
    }
    
    private int indexOf(int[] arr, int value) {
        for(int i=0; i<arr.length; i++) {
            if(arr[i]==value)
                return i;
        }
        return -1;
    }
}
