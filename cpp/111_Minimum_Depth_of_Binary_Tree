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
    int minDepth(TreeNode* root) {
        if(!root) return 0;
        int lmin = minDepth(root->left);
        int rmin = minDepth(root->right);
        return (lmin==0||rmin==0)?(lmin+rmin+1):(min(lmin, rmin)+1);
    }
};
