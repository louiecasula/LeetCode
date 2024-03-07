/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode a = head, b = head;
        int len = 1;
        while (true) {
            if (a.next != null && a.next.next != null) {
                a = a.next.next;
                len += 2;
                continue;
            }
            if (a.next != null) {
                a = a.next;
                len += 1;
                continue;
            }
            break;
        }
        for (int i = 0; i < len/2; i++) {
            b = b.next;
        }
        return b;
    }
}