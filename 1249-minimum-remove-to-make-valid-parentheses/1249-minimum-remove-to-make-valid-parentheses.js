/**
 * @param {string} s
 * @return {string}
 */
var minRemoveToMakeValid = function(s) {
    // Keep an output string and paren and thesis counters
    let out = "", paren = 0, thesis = 0;
    // Iterate, count theses
    for (let c of s) {
        if (c === ")") { thesis++; }
    }
    // Iterate again, count paren and add element to output if counts aren't equal
    for (let c of s) {
        if (c === "(") {
            if (paren === thesis) { continue; }
            paren++;
        } else if (c === ")") {
            thesis--;
            if (paren === 0) { continue; }
            paren--;
        } out += c;
    }
    // Return output string
    return out;
};