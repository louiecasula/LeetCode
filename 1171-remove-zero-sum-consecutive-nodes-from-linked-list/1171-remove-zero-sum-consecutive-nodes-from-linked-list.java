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
    public ListNode removeZeroSumSublists(ListNode head) {
        //// Hash table, prefix sum method ////
        // Make a dummy node and keep the prefix sum
        ListNode dummy = new ListNode(0, head);
        int prefixSum = 0;
        // Map the running sum with the head's value
        Map<Integer, ListNode> map = new HashMap();
        map.put(prefixSum, dummy);
        while (head != null) {
            prefixSum += head.val;
            map.put(prefixSum, head);
            head = head.next;
        }
        // Go through linked list again, making the next node equal to the map's value of the sum
        head = dummy;
        prefixSum = 0;
        while (head != null) {
            prefixSum += head.val;
            head.next = map.get(prefixSum).next;
            head = head.next;
        }
        return dummy.next;
    }
}