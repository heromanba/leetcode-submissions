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
    void visitAlongLeftBranch(
        TreeNode* x,  
        vector<int>& visited,
        stack<TreeNode*>& S
    )
    {
        while (x) {
            visited.push_back( x->val );
            S.push( x->right );
            x = x->left;
        }
    }
    
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> visited;
        stack<TreeNode*> S;
        
        TreeNode* x = root;
        while (true) {
            visitAlongLeftBranch( x, visited, S );
            if ( S.empty() ) break;
            x = S.top();
            S.pop();
        }
        return visited;
    }
};
