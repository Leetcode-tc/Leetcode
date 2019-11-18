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
    int sumOfLeftLeaves(TreeNode* root) {
        if(root==NULL||isLeaf(root)) return 0;
        int ret = 0;
        if(isLeaf(root->left)) ret += root->left->val;
        return ret+sumOfLeftLeaves(root->left)+sumOfLeftLeaves(root->right);
    }
    
    
    bool isLeaf(TreeNode *node){
        return node?(node->left==NULL&&node->right==NULL):false;
    }
};
