/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    var head = new ListNode(0);
    var p = head;
    var carry = 0;
    while(l1||l2){
        var sum = carry;
        if(l1){
            sum += l1.val;
            l1 = l1.next;
        }
        if(l2){
            sum += l2.val;
            l2 = l2.next;
        }
        
        carry = Math.floor(sum/10);
        sum %= 10;
        var temp = new ListNode(sum);
        p.next = temp;
        p = temp;
    }
    if(carry>0){
        var temp1 = new ListNode(carry);
        p.next = temp1;
    }
    return head.next;
};