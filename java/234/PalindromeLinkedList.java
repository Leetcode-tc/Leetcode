/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        // 如果是空链表或者单结点链表，默认为回文链表
        if (head == null || head.next == null) {
            return true;
        }
        // 使用快慢节点找到链表中点，并在过程中将链表前半段反序
        ListNode slow = head;
        ListNode fast = head;
        ListNode prev = null;
        while (fast != null && fast.next != null) {
            ListNode tmp = slow;
            slow = slow.next;
            fast = fast.next.next;
            tmp.next = prev;
            prev = tmp;
        }

        // 分为奇数个结点和偶数个结点两种情况讨论
        ListNode head1;
        ListNode head2;
        if (fast == null) {
            // 1.偶数个结点
            head1 = prev;
            head2 = slow;
        } else {
            // 2.奇数个结点
            head1 = prev;
            head2 = slow.next;
        }
        return compareTwoLink(head1, head2);
    }

    private boolean compareTwoLink(ListNode node1, ListNode node2) {
        while (node1 != null) {
            if (node1.val != node2.val) {
                return false;
            }
            node1 = node1.next; 
            node2 = node2.next;
        }
        return true;
    }
}
