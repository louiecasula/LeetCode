/**
 * @param {string} val
 * @return {Object}
 */
const expect = (val) => {
    return {
        toBe: (comp) => {
            if (val === comp) { return true; }
            throw new Error("Not Equal");
        },

        notToBe: (comp) => {
            if (val !== comp) { return true; }
            throw new Error("Equal");
        },
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */