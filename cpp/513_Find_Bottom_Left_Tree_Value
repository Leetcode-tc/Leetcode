/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        queue<TreeNode*> q;
        TreeNode *p = NULL;
        q.push(root);
        while(!q.empty()){
            p = q.front();
            q.pop();
            if(p->right) q.push(p->right);
            if(p->left) q.push(p->left);
        }
        return p->val;
    }
};
