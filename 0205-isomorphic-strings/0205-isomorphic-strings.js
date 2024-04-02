/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    // Keep a hash map for each word with the letter as key and a list of indexes as value
    let sMap = {}, tMap = {};
    // Iterate, updating both maps
    for (let i = 0; i < s.length; i++) {
        s[i] in sMap? sMap[s[i]].push(i): sMap[s[i]] = [i];
        t[i] in tMap? tMap[t[i]].push(i): tMap[t[i]] = [i]; 
        // If current elements values aren't equal in both maps, return false
        if (JSON.stringify(sMap[s[i]]) !== JSON.stringify(tMap[t[i]])) {
            return false;
        }
    }
    // Return true
    return true;
};