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
import java.math.BigInteger;

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // Add each val * increasing factor to a sum for each linked list
        BigInteger i1 = BigInteger.ZERO;
        BigInteger i2 = BigInteger.ZERO;
        BigInteger fact = BigInteger.ONE;
        while (l1 != null || l2 != null) {
            if (l1 != null) {
                i1 = i1.add(fact.multiply(BigInteger.valueOf(l1.val)));
                l1 = l1.next;
            }
            if (l2 != null) {
                i2 = i2.add(fact.multiply(BigInteger.valueOf(l2.val)));
                l2 = l2.next;
            }
            fact = fact.multiply(BigInteger.TEN);
        }
        // Add each ll num
        BigInteger sum = i1.add(i2);
        System.out.println(i1 + " + " + i2 + " = " + sum);
        // Save each digit as a new node and return the first node
        ListNode head = new ListNode((sum.mod(BigInteger.TEN)).intValue());
        ListNode curr = head;
        sum = sum.divide(BigInteger.TEN);
        while (sum.compareTo(BigInteger.ONE) >= 0) {
            curr.next = new ListNode((sum.mod(BigInteger.TEN)).intValue());
            curr = curr.next;
            sum = sum.divide(BigInteger.TEN);
        }
        return head;
    }
}