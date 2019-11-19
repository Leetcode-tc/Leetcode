/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode p = head;
        int carry = 0;
        while(l1!=null || l2!=null){
            int sum = carry;
            if(l1!=null){
                sum += l1.val;
                l1 = l1.next;
            }
            if(l2!=null){
                sum += l2.val;
                l2 = l2.next;
            }
            carry = sum/10;
            sum %= 10;
            p.next = new ListNode(sum);
            p = p.next;
        }
        if(carry>0){
            p.next = new ListNode(carry);
        }
        return head.next;
    }
}