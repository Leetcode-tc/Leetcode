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
    vector<int> findMode(TreeNode* root) {
        prev = NULL;
        prevCnt = 0;
        maxCnt = 0;
        inorder(root);
        return ret;
    }
    
    //中序遍历，prev记录前一节点，通过它来得到根节点值得数量
    void inorder(TreeNode *root){
        if(root==NULL) return;
        inorder(root->left);
        if(prev==NULL||prev->val!=root->val){
            prev = root;
            prevCnt = 0;
        }
        prevCnt++;
        if(prevCnt>maxCnt){
            ret.clear();
            ret.push_back(prev->val);
            maxCnt = prevCnt;
        }
        else if(prevCnt==maxCnt){
            ret.push_back(prev->val);
        }
        inorder(root->right);
    }
    
    
private:
    vector<int> ret;
    TreeNode *prev;
    int prevCnt;
    int maxCnt;
};
