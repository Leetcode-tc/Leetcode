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
    //中序遍历，用pre记录上一个遍历的结点，由于交换结点后会出现1或2处pre->val>=cur->val，1的情况就是两者在中序位置相邻,第一次出现的pre就是
    //错误结点1，第二次出现的root是错误结点2,找到两个结点之后交换值即可
    void recoverTree(TreeNode* root){
        findNodes(root);
        int t = node1->val;
        node1->val = node2->val;
        node2->val = t;
    }
    
    void findNodes(TreeNode* root) {
        if(root){
            findNodes(root->left);
            if(pre&&pre->val>=root->val){
                if(node1==NULL) node1 = pre;
                if(node1!=NULL) node2 = root;
            }
            pre = root;
            findNodes(root->right);
        }
    }
private:
    TreeNode *pre = NULL;
    TreeNode *node1 = NULL, *node2 = NULL;
};
