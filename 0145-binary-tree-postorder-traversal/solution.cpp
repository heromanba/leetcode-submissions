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
    bool isChild(TreeNode* child, TreeNode* parent)
    {
        return (parent->left == child) || (parent->right == child);
        
    }
    
    void gotoHLVFL(stack<TreeNode* >& S)
    {
        while (TreeNode* x = S.top())
        {
            if (x->left)
            {
                if (x->right)
                    S.push(x->right);
                S.push(x->left);
            } else
                S.push(x->right);
        }
        S.pop();    
    }
    
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> visited;
        stack<TreeNode* > S;
        TreeNode* x = root;
        
        if (x) S.push(x);
        
        while (!S.empty())
        {
            if (!isChild(x, S.top()))
                gotoHLVFL(S);
            x = S.top();
            S.pop();
            visited.push_back(x->val);
        }
        return visited;
    }
};
