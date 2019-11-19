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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head = new ListNode(0);
        ListNode *p = head;
        int carry = 0;
        while(l1 || l2 || carry>0){
            carry += getValue(l1)+getValue(l2);
            p->next = new ListNode(carry%10);
            p = p->next;
            l1 = getNext(l1);
            l2 = getNext(l2);
            carry /= 10;
        }
        p = head->next;
        delete head;
        return p;
    }
    
    int getValue(ListNode *p){
        return p==NULL?0:p->val;
    }
    
    ListNode* getNext(ListNode *p){
        return p==NULL?NULL:p->next;
    }
};