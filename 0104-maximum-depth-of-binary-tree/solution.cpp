/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int bottomUp(TreeNode* root) {
        if (!root)
            return 0;
        int left_depth = bottomUp(root->left);
        int right_depth = bottomUp(root->right);
        int depth = max(left_depth, right_depth) + 1;
        return depth;
    }
    
    int maxDepth(TreeNode* root) {
        return bottomUp(root);
        
    }
};
