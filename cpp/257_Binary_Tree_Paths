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
    vector<string> binaryTreePaths(TreeNode *root){
        vector<string> ret;
        if(!root) return ret;
        binaryTreePaths(root, ret, "");
        return ret;
    }
    
    void binaryTreePaths(TreeNode* root, vector<string> &ret, string s){
        if(root->left==NULL&&root->right==NULL){
            ret.push_back(s+to_string(root->val));
        }
        else{
            if(root->left)
                binaryTreePaths(root->left, ret, s+to_string(root->val)+"->");
            if(root->right)
                binaryTreePaths(root->right, ret, s+to_string(root->val)+"->");
        }
    }
    
    vector<string> binaryTreePaths1(TreeNode* root) {
        vector<string> ret;
        vector<TreeNode*> v;
        TreeNode *p = root, *r = NULL;
        while(p||!v.empty()){
            if(p){
                v.push_back(p);
                p = p->left;
            }
            else{
                p = v.back();
                if(p->right&&r!=p->right)
                    p = p->right;
                else{
                    if(p->left==NULL&&p->right==NULL){
                        ret.push_back(visit(v));
                    }
                    v.pop_back();
                    r = p;
                    p = NULL;
                }
                
            }
        }
        return ret;
    }
    
    string visit(vector<TreeNode*> &v){
        string s = "";
        for(int i=0;i<v.size();++i){
            s += to_string(v[i]->val);
            if(i!=v.size()-1)
                s += "->";
        }
        return s;
    }
};
