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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // Determine starting node
        ListNode start;
        if (list1 == null && list2 == null) { return null; }
        if (list1 == null) { return list2; }
        if (list2 == null) { return list1; }
        if (list1.val <= list2.val) {
            start = list1;
            list1 = list1.next;
        } else {
            start = list2;
            list2 = list2.next;
        }
        ListNode head = start;
        // Iterate until the end of both lls
        while (list1 != null || list2 != null) {
            // If list2's val comes before list1's val, current node's next is list2's val
            if (list1 == null) {
                head.next = list2;
                head = head.next;
                list2 = list2.next;
            }
            else if (list2 == null) {
                head.next = list1;
                head = head.next;
                list1 = list1.next;
            }
            else if (list2.val <= list1.val) {
                head.next = list2;
                head = head.next;
                list2 = list2.next;
            } else {
                head.next = list1;
                head = head.next;
                list1 = list1.next;
            }
        }
        // Return starting node
        return start;
    }
}