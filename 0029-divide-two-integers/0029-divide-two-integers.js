/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    if (dividend == (2**31 * -1) && divisor == -1) { return 2**31 -1; }
    let pos = (dividend > 0) == (divisor > 0);
    let quotient = 0;
    dividend = Math.abs(dividend), divisor = Math.abs(divisor);
    while (dividend - divisor >= 0) {
        let ndivisor = divisor;
        let factor = 0;
        while (dividend - (ndivisor * 2) >= 0) {
            ndivisor *= 2;
            factor++;
        }
        dividend -= ndivisor;
        quotient += 2**factor;
    }
    if (!pos) {
        quotient *= -1;
    }
    return quotient;
};