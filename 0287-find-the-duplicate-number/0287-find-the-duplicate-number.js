/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    //// Linked List, Floyd's Cycle Method ////
    // Iterate with slow and fast pointers until they intersect
    let slow = 0, fast = 0;
    do {
        slow = nums[slow];
        fast = nums[nums[fast]];
    } while (slow !== fast);
    // Iterate from the beginning and from the intersection, return the new intersection
    let slow2 = 0;
    while (slow !== slow2) {
        slow = nums[slow];
        slow2 = nums[slow2];
    }
    return slow;
};