/**
 * @param {number} n
 * @return {number}
 */
var pivotInteger = function(n) {
    let arr = [];
    let pref_sum = 0;
    let total = n * (n + 1) / 2;
    for (let i = 1; i <= n; i++) { arr.push(i); };
    // Iterate from 1 -> n
    for (let i = 0; i < n; i++) {
        // If sum 1 -> i == sum i -> n, return i
        pref_sum += i + 1;
        if (pref_sum === total - pref_sum + i + 1) {
            return i + 1;
        }
    }
    // Return -1
    return -1;
}