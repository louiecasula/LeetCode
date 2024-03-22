/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    //// Meet in the Middle Method ////
    // Iterate to end of ll with fast an slow nodes
    let fast = head, slow = head;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }
    // Set middle's next to null
    let prev = slow;
    slow = slow.next;
    prev.next = null;
    // Iterate the second half, making each node point towards middle
    while (slow) {
        let temp = slow.next;
        slow.next = prev;
        prev = slow;
        slow = temp;
    }
    // Iterate head and tail towards middle
    while (prev) {
        // If values are diff, return false
        if (prev.val !== head.val) { return false; }
        head = head.next;
        prev = prev.next;
    }
    // Return true
    return true;
};