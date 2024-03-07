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
            System.out.println(a.val);
            if (a.next != null && a.next.next != null && a.next.next.next != null && a.next.next.next.next != null && a.next.next.next.next.next != null) {
                a = a.next.next.next.next.next;
                len += 5;
                continue;
            }
            if (a.next != null && a.next.next != null && a.next.next.next != null && a.next.next.next.next != null) {
                a = a.next.next.next.next;
                len += 4;
                continue;
            }
            if (a.next != null && a.next.next != null && a.next.next.next != null) {
                a = a.next.next.next;
                len += 3;
                continue;
            }
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