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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return buildTree(preorder, 0, preorder.size()-1, inorder, 0, inorder.size()-1);
    }

    TreeNode* buildTree(vector<int> &preorder, int lp, int rp, vector<int> &inorder, int li, int ri){
        if(lp>rp) return NULL;
        TreeNode *root = new TreeNode(preorder[lp]);
        int i = li;
        while(inorder[i]!=preorder[lp])
            i++;
        root->left = buildTree(preorder, lp+1, lp+i-li, inorder, li, i-1);
        root->right = buildTree(preorder, lp+i-li+1, rp, inorder, i+1, ri);
        return root;
    }
};
