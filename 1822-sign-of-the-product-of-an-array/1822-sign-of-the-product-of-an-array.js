/**
 * @param {number[]} nums
 * @return {number}
 */
var arraySign = function(nums) {
    // Count nums that are negative
    let count = 0;
    for (let num of nums) {
        // If there's a 0, return 0
        if (num === 0) { return 0; }
        if (num < 0) { count++; }
    }
    // If count is even return 1, else return -1
    return (count % 2 === 0)? 1: -1;
};