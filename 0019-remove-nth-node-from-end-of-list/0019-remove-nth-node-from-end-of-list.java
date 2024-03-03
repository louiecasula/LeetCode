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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // Use two pointers separated by a length of n
        ListNode i = head, j = head;
        int count = 0;
        while (i.next != null) {
            if (count >= n) {
                j = j.next;
            }
            count++;
            i = i.next;
        }
        // For deletion
        if (j == head && count != n) { return head.next; }
        if (j.next != null) { j.next = j.next.next; }
        return head;
    }
}