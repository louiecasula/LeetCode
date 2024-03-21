/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    // Edgecase
    if (dividend == (2**31 * -1) && divisor == -1) { return 2**31 -1; }
    // Set a boolean for pos or neg sign quotient and keep a quotient(counter) variable
    let pos = (dividend > 0) == (divisor > 0);
    let quotient = 0;
    // Make dividend & divisor positive regardless of original sign
    dividend = Math.abs(dividend), divisor = Math.abs(divisor);
    // While the dividend - divisor is at least 0,
    while (dividend - divisor >= 0) {
        let ndivisor = divisor;
        let factor = 0;
        // While the dividend - divisor * 2 is at least 0, keep doubling divisor, increment a factor variable
        while (dividend - (ndivisor * 2) >= 0) {
            ndivisor *= 2;
            factor++;
        }
        // Set the dividend as the difference between the highest doubled divisor and the dividend
        dividend -= ndivisor;
        quotient += 2**factor;
    }
    // Make the quotient negative if applicable and return
    if (!pos) {
        quotient *= -1;
    }
    return quotient;
};