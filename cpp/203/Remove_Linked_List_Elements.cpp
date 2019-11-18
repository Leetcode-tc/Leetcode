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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *t = new ListNode(0);
        t->next = head;
        ListNode *pre = t;
        while(head){
            if(head->val==val){
                pre->next = head->next;
                delete head;
                head = pre->next;
            }
            else{
                pre = head;
                head = head->next;
            }
        }
        head = t->next;
        delete t;
        return head;
    }
};
