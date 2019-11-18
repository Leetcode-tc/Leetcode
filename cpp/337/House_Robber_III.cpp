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
    //比较直接简单的做法，对于根为root的树T，令M(root)为该问题的解，则有以下两种情况：
    //包含root，此时   M(withRoot)=root->val+M(root->left->left)+M(root->left->right)+M(root->right->left)+M(root->right+right)
    //不包含root,     M(withoutRoot)=M(root->left)+M(root->right)
    //最终的解是 max(M(withRoot),M(withoutRoot))
    //这里含有很多重复的子问题，比如在计算M(root->left)时又会计算M(root->left->left),M(root->left->right)，导致重复，效率低。
    int rob(TreeNode* root) {
        if(!root) return 0;
        if(root->left==NULL&&root->right==NULL)
            return root->val;
        int withRoot = root->val, withoutRoot = 0;
        if(root->left){
            withRoot += rob(root->left->left)+rob(root->left->right);
            withoutRoot += rob(root->left);
        }
        if(root->right){
            withRoot += rob(root->right->left)+rob(root->right->right);
            withoutRoot += rob(root->right);
        }
        return max(withRoot, withoutRoot);
    }
    
    //为了减少重复计算，用dp记录下计算过的子问题
    int rob(TreeNode* root, map<TreeNode*,int> &dp) {
        if(!root) return 0;
        if(dp.find(root)!=dp.end())
            return dp[root];
        int withRoot = root->val, withoutRoot = 0;
        if(root->left){
            withRoot += rob(root->left->left, dp)+rob(root->left->right, dp);
            withoutRoot += rob(root->left, dp);
        }
        if(root->right){
            withRoot += rob(root->right->left, dp)+rob(root->right->right, dp);
            withoutRoot += rob(root->right, dp);
        }
        dp[root] = max(withRoot,withoutRoot);
        return dp[root];
    }
    
    //计算子问题过程中记录值
    int rob(TreeNode *root, int &withRoot, int &withoutRoot){
        if(!root) return 0;
        int lwithRoot=0, lwithoutRoot=0, rwithRoot=0, rwithoutRoot=0;
        
        rob(root->left, lwithRoot, lwithoutRoot);
        rob(root->right, rwithRoot, rwithoutRoot);
        
        withRoot = root->val+lwithoutRoot+rwithoutRoot;
        withoutRoot = max(lwithRoot, lwithoutRoot)+max(rwithRoot, rwithoutRoot);
        
        return max(withRoot, withoutRoot);
    }
};
