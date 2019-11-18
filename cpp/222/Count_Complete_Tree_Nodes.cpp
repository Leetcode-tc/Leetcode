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
    int countNodes(TreeNode* root) {
        if(!root) return 0;
        TreeNode *l = root, *r = root;
        int depth = 0;
        while(r){
            l = l->left;
            r = r->right;
            depth++;
        }
        if(!l) return pow(2, depth)-1;
        return 1+countNodes(root->left)+countNodes(root->right);
    }
};
