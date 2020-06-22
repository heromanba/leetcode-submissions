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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> vec_root;
        if (root == NULL)
            return vec_root;
        
        vector<int> vec_left;
        vector<int> vec_right;
        
        if (root->left != NULL)
            vec_left = preorderTraversal(root->left);
        if (root->right != NULL)
            vec_right = preorderTraversal(root->right);
        vec_root.push_back(root->val);
        
        vec_root.reserve(vec_root.size() + vec_left.size() + vec_right.size());
        
        vec_root.insert(vec_root.end(), vec_left.begin(), vec_left.end());
        vec_root.insert(vec_root.end(), vec_right.begin(), vec_right.end());
        return vec_root;
    }
};
