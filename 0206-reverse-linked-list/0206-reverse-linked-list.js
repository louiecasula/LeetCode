/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    if (head === null) { return null; }
    if (head.next === null) { return head; }
    let tail = head, prev = head;
    head = head.next;
    tail.next = null;
    while (head.next != null) {
        prev = head;
        head = head.next;
        prev.next = tail;
        tail = prev;
    }
    head.next = prev;
    return head;
};