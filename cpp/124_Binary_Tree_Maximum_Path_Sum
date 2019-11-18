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
    int maxPathSum(TreeNode* root) {
        int ret = INT_MIN;
        maxPathSum(root, ret);
        return ret;
    }
    //每一个节点都可能是最大sum路径中的最高节点，所以遍历每个节点时都看一下包含该节点的最大路径和是否为最大
    //返回包含当前节点的“单向”路径中的最大路径值,如果该值为负，则舍弃，用0代替
    int maxPathSum(TreeNode *root, int &maxSum){
        if(!root)
            return 0;
        int lmax = max(0, maxPathSum(root->left, maxSum));
        int rmax = max(0, maxPathSum(root->right, maxSum));
        maxSum = max(maxSum, lmax+rmax+root->val);
        return max(lmax, rmax)+root->val;
    }
};
