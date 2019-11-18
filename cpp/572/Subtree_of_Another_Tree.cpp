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
    bool isSubtree(TreeNode* s, TreeNode* t) {
        if(!s&&!t) return true;
        if(!s||!t) return false;
        if(s->val==t->val&&isSametree(s, t)){
            return true;
        }
        return isSubtree(s->left, t)||isSubtree(s->right, t);
    }
    
    bool isSametree(TreeNode *t1, TreeNode *t2){
        if(!t1&&!t2) return true;
        if(!t1||!t2) return false;
        return t1->val==t2->val&&isSametree(t1->left, t2->left)&&isSametree(t1->right, t2->right);
    }
};

