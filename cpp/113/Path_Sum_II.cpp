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
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> ret;
        vector<int> v;
        pathSum(root, sum, ret, v);
        return ret;
    }
    //深度优先搜索，遍历过程中记录路过节点的值，到达叶子节点时，将当前路径进行记录
    void pathSum(TreeNode* root, int sum, vector<vector<int>> &ret, vector<int> &v){
        if(root){
            v.push_back(root->val);
            if(root->left==NULL&&root->right==NULL&&sum==root->val){
                ret.push_back(v);
            }
            pathSum(root->left, sum-root->val, ret, v);
            pathSum(root->right, sum-root->val, ret, v);
            v.pop_back();
        }
    }
};
