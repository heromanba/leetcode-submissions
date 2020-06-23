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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if (root == NULL)
            return result;
        
        std::queue<TreeNode*> q_node;
        std::queue<int> q_level;    // Record corresponding level of the node.
        
        // Initialize the queue.
        q_node.push(root);
        q_level.push(1);
        
        while (!q_node.empty())
        {
            // Get the first value of the queue.
            TreeNode* node = q_node.front();
            int level = q_level.front();
            
            // Push a new vector for the next level.
            if (level > result.size())
            {
                vector<int> tmp_vec;
                result.push_back(tmp_vec);
            }
            
            // Push value into vector of the current level.
            if (level == result.size())
            {
                result[level - 1].push_back(node->val);
            }
            
            q_node.pop();
            q_level.pop();
            
            if (node->left != NULL)
            {
                q_node.push(node->left);
                q_level.push(level + 1);
            }
            if (node->right != NULL)
            {
                q_node.push(node->right);
                q_level.push(level + 1);
            }
            
        }
        
        return result;
    }
};
