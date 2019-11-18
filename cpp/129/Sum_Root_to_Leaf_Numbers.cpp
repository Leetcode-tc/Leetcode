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
    int sumNumbers(TreeNode* root) {
        int currentSum = 0, ret = 0;
        sumNumbers(root, currentSum, ret);
        return ret;
    }
    //后续遍历，到达子节点时，累加新的值
    void sumNumbers(TreeNode *root, int currentSum, int &ret){
        if(root){
            currentSum = currentSum*10+root->val;
            sumNumbers(root->left, currentSum, ret);
            sumNumbers(root->right, currentSum, ret);
            if(root->left==NULL&&root->right==NULL)
                ret += currentSum;
        }
    }
};
