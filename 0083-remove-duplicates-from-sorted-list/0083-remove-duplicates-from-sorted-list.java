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
    public ListNode deleteDuplicates(ListNode head) {
        // Edgecase
        if (head == null) { return null; }
        // Iterate through nodes
        ListNode dummy = head;
        ListNode next = head;
        while (next != null) {
            // If next's val == current's val, skip
            while (next != null && next.val == dummy.val) {
                next = next.next;
            }
            dummy.next = next;
            dummy = next;
        }
        // Return head
        return head;
    }
}