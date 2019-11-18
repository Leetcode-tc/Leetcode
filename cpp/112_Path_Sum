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
    //遍历二叉树，到叶子节点时判断
    bool hasPathSum(TreeNode* root, int sum) {
        if(root){
            if(root->left==NULL&&root->right==NULL&&sum==root->val)
                return true;
            return hasPathSum(root->left, sum-root->val) ||
                    hasPathSum(root->right, sum-root->val);
        }
        return false;
    }
};
