/**
 * @param {number[]} nums
 * @return {number}
 */
let subsetXORSum = function(nums) {
    // Use output, subset, and index variables as parameters for backtracking function
    let subset = [], index = 0;
    return calcSubsetXOR(nums, subset, index);
};

// Iterate through all subsets, adding each one's XOR total to eachother
let calcSubsetXOR = function(nums, subset, index) {
    // Add current subset's XOR total to output
    let xor = 0;
    for (let i = 0; i < subset.length; i++) {
        xor ^= subset[i];
    }
    let out = xor;
    // Recursively generate subsets by including and excluding elements
    for (let i = index; i < nums.length; i++) {
        subset.push(nums[i]);
        out += calcSubsetXOR(nums, subset, i + 1);
        subset.pop();
    }
    // Returning running sum
    return out;
};