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
    bool isSymmetric(TreeNode* root) {
        if(!root) return true;
        return isSymmetric(root->left, root->right);
    }
    //递归版本
    bool isSymmetric(TreeNode *lchild, TreeNode *rchild){
        if(lchild==NULL&&rchild==NULL)
            return true;
        if(lchild==NULL||rchild==NULL)
            return false;
        return lchild->val==rchild->val&&isSymmetric(lchild->left, rchild->right)
                &&isSymmetric(lchild->right, rchild->left);
    }
    //非递归
    bool isSymmetric(TreeNode *root){
        if(!root) return true;
        vector<TreeNode*> v{root->left, root->right};
        while(v.size()>0){
            int n = v.size();
            if(n>1&&(n&0x1)){
                return false;
            }
            vector<TreeNode*> vl, vr;
            for(int i=0,j=n-1;i<j;i++,j--){
                if(v[i]==NULL&&v[j]==NULL) continue;
                if(v[i]==NULL||v[j]==NULL||v[i]->val!=v[j]->val)
                    return false;
                vl.push_back(v[i]->left);
                vl.push_back(v[i]->right);
                vr.push_back(v[j]->right);
                vr.push_back(v[j]->left);
            }
            v.clear();
            v.insert(v.end(), vl.begin(), vl.end());
            v.insert(v.end(), vr.rbegin(), vr.rend());
        }
        return true;
    }
};
