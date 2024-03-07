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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // Add each val * increasing factor to a sum for each linked list
        boolean carry = (l1.val + l2.val) > 9;
        ListNode head = new ListNode((l1.val + l2.val) % 10);
        ListNode curr = head;
        l1 = l1.next;
        l2 = l2.next;
        while ((l1 != null || l2 != null) || carry) {
            curr.next = new ListNode(0);
            curr = curr.next;
            if (carry) {
                curr.val += 1;
                carry = false;
            }
            if (l1 == null && l2 != null) {
                curr.val += l2.val;
            }
            if (l1 != null && l2 == null) {
                curr.val += l1.val;
            }
            if (l1 != null && l2 != null) {
                curr.val += l1.val + l2.val;
            }
            if (curr.val > 9) {
                curr.val = curr.val % 10;
                carry = true;
            }
            if (l1 != null) { l1 = l1.next; }
            if (l2 != null) { l2 = l2.next; }
        }
        return head;
    }
}