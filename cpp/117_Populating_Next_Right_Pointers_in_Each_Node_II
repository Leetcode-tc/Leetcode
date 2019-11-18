/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    //层序遍历，可以通过next来代替队列
    void connect(TreeLinkNode *root) {
        while(root){
            TreeLinkNode *head = new TreeLinkNode(0);
            TreeLinkNode *pre = head, *cur = root;
            while(cur){
                if(cur->left){
                    pre->next = cur->left;
                    pre = pre->next;
                }
                if(cur->right){
                    pre->next = cur->right;
                    pre = pre->next;
                }
                cur = cur->next;
            }
            root = head->next;
            delete head;
        }
    }
};
