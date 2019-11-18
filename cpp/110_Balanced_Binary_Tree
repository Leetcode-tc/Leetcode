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
    //深度优先遍历，过程中将每个节点的值记录为当前树的高度，随即可以通过左右子节点的高度值
    //判断是否平衡，并且计算自身高度
    bool isBalanced(TreeNode* root) {
        if(!root)
            return true;
        if(!isBalanced(root->left)||!isBalanced(root->right))
            return false;
        int lh = root->left?root->left->val:0;
        int rh = root->right?root->right->val:0;
        root->val = max(lh, rh)+1;
        return abs(lh-rh)<=1;
    }
};
