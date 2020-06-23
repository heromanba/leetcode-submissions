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
    bool isTwoTreeMirror(TreeNode* left, TreeNode* right) {
        if ((left == NULL) && (right == NULL))
            return true;
        if ((left == NULL) || (right == NULL))
            return false;
        return isTwoTreeMirror(left->left, right->right) && 
            isTwoTreeMirror(left->right, right->left) &&
            (left->val == right->val);
    }
    
    bool isSymmetric(TreeNode* root) {
        
        return isTwoTreeMirror(root, root);
    }
};
