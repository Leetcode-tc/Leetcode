/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *p = NULL;
    bool isPalindrome(ListNode* head) {
        p = head;
        return check(head);
    }
    
    bool check(ListNode *q){
        if(!q) return true;
        bool ret = check(q->next)&(p->val==q->val);
        p = p->next;
        return ret;
    }
};
