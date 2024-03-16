/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxLength = function(nums) {
    // Keep a running sum where 1 = 1, 0 = -1
    const ind_map = new Map();
    let s = out = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 0) { s--; } 
        else { s++; }
        // Map the index at each new sum
        if (!ind_map.has(s)) { ind_map.set(s, i); }
        // If sum is zero, make output the current length
        if (s === 0) { out = i + 1; }
        // Else, make output the greater of the current map value and current output
        out = Math.max(out, i - ind_map.get(s));
    };
    return out;
};