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
        //// Convert to array
        ArrayList<Integer> array = new ArrayList();
        ListNode curr = head;
        while (curr != null) {
            array.add(curr.val);
            curr = curr.next;
        }
        //// While there is a subarray that sums to zero, delete it
        // Nested for loop
        for (int i = 0; i < array.size() - 1; i++) {
            int sum = array.get(i);
            for (int j = i + 1; j < array.size(); j++) {
                sum += array.get(j);
                // If sum equals 0, 
                if (sum == 0) {
                    for (int k = i; k <= j; k++) {
                        array.set(k, 0);
                    }
                    i = j;
                    break;
                }
            }
        }
        array.removeAll(Arrays.asList(0));
        if (array.size() == 0) { return null; }
        //// Convert back to linked list (recycle the original (; )
        curr = head;
        for (int i = 0; i < array.size(); i++) {
            if (array.get(i) != 0) {
                curr.val = array.get(i);
                if (i != array.size() - 1) {
                    curr = curr.next;
                }
            }
        }
        curr.next = null;
        return head;
    }
}