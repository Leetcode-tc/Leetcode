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
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return sortedArrayToBST(nums, 0, nums.size()-1);
    }
    //用中位数建立根节点，用左右子数组分别建立左右子树，递归直到建立整棵树
    TreeNode* sortedArrayToBST(vector<int> &nums, int l, int r){
        if(l>r) return NULL;
        int m = l + (r-l)/2;
        TreeNode *root = new TreeNode(nums[m]);
        root->left = sortedArrayToBST(nums, l, m-1);
        root->right = sortedArrayToBST(nums, m+1, r);
        return root;
    }
};
