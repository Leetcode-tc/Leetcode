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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return buildTree(inorder, 0, inorder.size()-1, postorder, 0, postorder.size()-1);
    }
    
    TreeNode* buildTree(vector<int> &inorder, int li, int ri, vector<int> &postorder, int lp, int rp){
        if(li>ri) return NULL;
        TreeNode *root = new TreeNode(postorder[rp]);
        int i = li;
        while(inorder[i]!=postorder[rp])
            i++;
        root->left = buildTree(inorder, li, i-1, postorder, lp, lp+i-li-1);
        root->right = buildTree(inorder, i+1, ri, postorder, lp+i-li, rp-1);
        return root;
    }
};
