/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function(s, t) {
    // Sort both strings
    s = s.split("").sort();
    t = t.split("").sort();
    console.log(s)
    console.log(t)
    // Iterate, if t's element doesn't equal s', return it
    for (let i = 0; i < t.length; i++) {
        if (s[i] !== t[i]) { return t[i]; }
    }
};