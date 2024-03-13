/**
 * @param {number} n
 * @return {number}
 */
var pivotInteger = function(n) {
    let arr = [];
    for (let i = 1; i <= n; i++) { arr.push(i); };
    // Iterate from 1 -> n
    for (let i = 0; i < n; i++) {
        // If sum 1 -> i == sum i -> n, return i
        if (arr.slice(0, i + 1).reduce((sum, curr) => sum + curr) === 
        arr.slice(i, n).reduce((sum, curr) => sum + curr)) {
            return i + 1;
        }
    }
    // Return -1
    return -1;
}