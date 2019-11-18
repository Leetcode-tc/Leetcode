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
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution(ListNode* head) {
        this->head = head;
    }
    
    /** Returns a random node's value. */
    int getRandom() {
        ListNode *p = head;
        int ret = p->val;
        int i = 2;
        srand(time(NULL));
        while(p->next){
            p = p->next;
            if(rand()%i+1==i)
                ret = p->val;
            i++;
        }
        return ret;
    }
    
private:
    ListNode *head = NULL;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */
