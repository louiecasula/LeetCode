/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    // Sort array
    citations = citations.sort(function(a,b){return a - b})
    n = citations.length;
    // Iterate
    for (let i = 0; i < n; i++)
        // If current val >= n - i, return n - i
        if (citations[i] >= n - i) { return n - i; }
    return 0;
};