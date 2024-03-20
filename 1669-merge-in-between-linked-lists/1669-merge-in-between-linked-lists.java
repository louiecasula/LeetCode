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
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        // Keep an index variable and save the list1's head
        ListNode head = list1;
        ListNode stop = new ListNode();
        ListNode cont = new ListNode();
        int i = 0;
        // Iterate list1 with two pointers, one stops at i = a - 1, one at i = b + 1
        while (list1 != null) {
            if (i == a - 1) {
                stop = list1;
            }
            if (i == b + 1) {
                cont = list1;
            }
            list1 = list1.next;
            i++;
        }
        // When b pointer stops, set a.next to list2 and iterate,
        stop.next = list2;
        while (list2.next != null) {
            list2 = list2.next;
        }
        // When at the end, set next to b
        list2.next = cont;
        // Return list1's head
        return head;
    }
}