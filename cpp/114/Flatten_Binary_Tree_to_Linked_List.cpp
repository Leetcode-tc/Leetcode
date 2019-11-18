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
    //往右遍历，对于每一个有左子树的节点，将左子树接到自己和右子树之间
    void flatten(TreeNode* root) {
        while(root){
            if(root->left){
                TreeNode *p = root->left;
                while(p->right){
                    p = p->right;
                }
                p->right = root->right;
                root->right = root->left;
                root->left = NULL;
            }
            root = root->right;
        }
    }
};
