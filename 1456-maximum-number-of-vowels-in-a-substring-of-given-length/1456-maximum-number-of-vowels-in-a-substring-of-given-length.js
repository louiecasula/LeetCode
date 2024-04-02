/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxVowels = function(s, k) {
    // Keep an output, vCount, list of vowels
    let vCount = 0, v = ['a','e','i','o','u'];
    // Iterate up to k, updating vCount
    for (let i = 0; i < k; i++) {
        if (v.includes(s[i])) { vCount++; }
    }
    if (vCount == k) { return vCount; }
    let out = vCount;
    // Iterate from k to end, updating vCount
    for (let i = k; i < s.length; i++) {
        if (v.includes(s[i - k])) { vCount--; }
        if (v.includes(s[i])) { vCount++; }
        // If vCount > output, update output
        out = Math.max(out, vCount);
        // If output == k, return output
        if (out == k) { return out; }
    }
    // Return output
    return out;
};