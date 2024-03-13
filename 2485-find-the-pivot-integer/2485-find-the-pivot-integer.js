/**
 * @param {number} n
 * @return {number}
 */
var pivotInteger = function(n) {
    let arr = [];
    let pref_sum = 0;
    let total = n * (n + 1) / 2;
    // Iterate from 1 -> n
    for (let i = 1; i <= n; i++) {
        // If sum 1 -> i == sum i -> n, return i
        pref_sum += i;
        if (pref_sum === total - pref_sum + i) {
            return i;
        }
    }
    // Return -1
    return -1;
}