/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // 为了避免对删除头指针的情况额外处理，设置哨兵结点
        ListNode preHead = new ListNode(-1);
        preHead.next = head;
        // 快指针比慢指针快n步，这样快指针指向最后一个结点时，慢指针指向要删除的前一个结点
        ListNode slow = preHead;
        ListNode fast = preHead;
        while (n > 0) {
            if (fast.next == null) {
                return preHead.next;
            }
            fast = fast.next;
            n--;
        }

        // 使快指针指向最后一个结点
        while (fast.next != null) {
            slow = slow.next;
            fast = fast.next;
        }
        // 删除结点
        slow.next = slow.next.next;

        return preHead.next;
    }
}
