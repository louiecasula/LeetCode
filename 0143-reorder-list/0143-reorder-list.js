/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
    //// No extra space method ////
    // Iterate ll with fast and slow pointers
    let slow = head, fast = head.next;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }
    let temp = slow.next;
    slow.next = null;
    slow = temp;
    // Reverse second half of ll
    let prev = null;
    while (slow) {
        temp = slow.next;
        slow.next = prev;
        prev = slow;
        slow = temp;
    }
    // Merge halves by alternating nodes
    while (head) {
        temp = head.next;
        head.next = prev;
        prev = temp;
        head = head.next;
    }
};