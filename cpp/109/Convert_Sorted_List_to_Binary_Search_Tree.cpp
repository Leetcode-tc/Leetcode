/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
    //深度优先，取中位数作为当前节点，用左右两边的子数组生成左右子树
    TreeNode* sortedListToBST(ListNode* head) {
        vector<int> v;
        while(head){
            v.push_back(head->val);
            head = head->next;
        }
        return sortedListToBST(v, 0, v.size()-1);
    }
    
    TreeNode* sortedListToBST(vector<int> &v, int l, int r){
        if(r<l){
            return NULL;
        }
        else{
            int m = l+(r-l)/2;
            TreeNode *root = new TreeNode(v[m]);
            root->left = sortedListToBST(v, l, m-1);
            root->right = sortedListToBST(v, m+1, r);
            return root;
        }
    }
};
