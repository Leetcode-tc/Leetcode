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
    int findMin(TreeNode *root){
        while(root&&root->left){
            root = root->left;
        }
        return root->val;
    }
    
    int findMax(TreeNode *root){
        while(root&&root->right){
            root = root->right;
        }
        return root->val;
    }
    //先判断子树是否为BST，如果是，则取左子树的最大值，比较其是否小于根的值，取右子树的最小值，看是否大于根的值
    bool isValidBST(TreeNode* root) {
        if(!root){
            return true;
        }
        if(!isValidBST(root->left)||!isValidBST(root->right)){
            return false;
        }
        if(root->right&&root->val>=findMin(root->right)||
        root->left&&root->val<=findMax(root->left)){
            return false;
        }
        return true;
    }
};
