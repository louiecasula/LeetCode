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
    // Iterate through ll, save each node val to an arr
    let dummy = head;
    let arr = [];
    while (dummy) {
        arr.push(dummy.val);
        dummy = dummy.next;
    }
    // Iterate ll again, change vals using a deque
    let i = 0;
    while (head) {
        head.val = i % 2 === 0? arr.shift(): arr.pop();
        i++;
        head = head.next;
    }
};