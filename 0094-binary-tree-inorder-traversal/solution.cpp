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
private:
    void goAlongLeftBranch(TreeNode* x, stack<TreeNode* >& S)
    {
        while(x) 
        {
            S.push(x);
            x = x->left;
        }
    }
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> visited;
        TreeNode* x = root;
        stack<TreeNode* > S;
        
        while (true)
        {
            goAlongLeftBranch(x, S);
            if (S.empty()) break;
            x = S.top();
            S.pop();
            visited.push_back(x->val);
            x = x->right;
        }
        return visited;
    }
};
