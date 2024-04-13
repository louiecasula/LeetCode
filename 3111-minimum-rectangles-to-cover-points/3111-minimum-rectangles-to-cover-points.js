/**
 * @param {number[][]} points
 * @param {number} w
 * @return {number}
 */
var minRectanglesToCoverPoints = function(points, w) {
    // Keep an output counter
    let out = 1;
    // Sort points by x value
    xVals = points.sort((a, b) => a[0] - b[0]);
    // Iterate x vals,
    let start = xVals.shift()[0];
    while (xVals.length > 0) {
        // If next val is > start + w, increment output, set new start
        let curr = xVals.shift()[0];
        if (curr > start + w) {
            out++;
            start = curr;
        }
    }
    // Return output
    return out;
};