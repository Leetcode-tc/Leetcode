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
    int findTilt(TreeNode* root) {
        int tilt = 0;
        findTilt(root, tilt);
        return tilt;
    }
    
    int findTilt(TreeNode *root, int &tilt){
        if(!root) return 0;
        int l = findTilt(root->left, tilt);
        int r = findTilt(root->right, tilt);
        tilt += abs(l-r);
        return l+r+root->val;
    }
};
